# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bs4 import BeautifulSoup as bs
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Phone
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
)
import requests
import json
from django.core import serializers
import urllib
import lxml.html
from rating.models import Rating
from phone.models import Phone
from appuser.models import Appuser
from django.db.models import Q

# import ssl
# Create your views here.
def returnall(req):
    if req.method == "POST":
        keyword = req.POST.get('searchkeyword')
        # get all the attribute names
        # attr = [obj.name for obj in Phone._meta.get_fields()] 
        # ty = [Phone._meta.get_field(name).get_internal_type for name in attr]
        # print (ty)
        thelist = Phone.objects.filter(Q(Model__icontains = keyword))
    else:
        keyword = None
        thelist = Phone.objects.all().order_by("Brand")
    ctx= {
        "accstatus" : req.user.is_authenticated,
        "list" : thelist,
        "keyword" : keyword
    }
    return render(req, "listofphones.html", ctx)
# returning all model name in list for autocomplete
def returnallmodel(req):
    model_s = []
    model = list(Phone.objects.order_by().values_list('Model').distinct())
    for i in model:
        model_s.append(i[0])
    # print (model)
    return JsonResponse(model_s, safe=False)

# returning content of model
def returnmcontent(req):
    print ("is inside returnmcontent")
    pk = req.GET.get('pk', None)
    model = Phone.objects.filter(pid = pk)
    print (model)
    model_s = serializers.serialize('json', list(model), fields=('Screen_size', 'Fingerprint_Authentication', 'Dual_Sim_card', 'Micro_sd', 'Battery_Capacity', 'Operating_System'))
    return JsonResponse(model_s, safe=False)
    
# returning model of specific brand
def returnmodel(req):
    brand = req.GET.get('brand', None)
    model = Phone.objects.filter(Brand = brand)
    # model = [rem[0] for rem in model]
    print (model)
    model_s = serializers.serialize('json', list(model), fields=('Model', 'pid',))
    return JsonResponse(model_s, safe=False)

def filterfunc(req):
    if req.method == "POST":
        # should access form info here
        # here it reads the filter value which can further trigger Phone.object.filter(Screen_size = variable)
         
        current_phone_data = Phone.objects.filter(pk = req.POST.get("modelname")).values('Screen_size', 'Battery_Capacity')
        
        criteria = []

        if (req.POST.get("screen") == ">"):
            criteria.append("Screen_size__gte=" + str(current_phone_data[0]['Screen_size']))
        elif (req.POST.get("screen") == "<"):
            criteria.append("Screen_size__lte=" + str(current_phone_data[0]['Screen_size']))
        elif (req.POST.get("screen") == "="):
            criteria.append("Screen_size=" + current_phone_data[0]['Screen_size'])

        criteria.append("Fingerprint_Authentication" + "=" + req.POST.get("fingerprint")) if (req.POST.get("fingerprint") != "/") else ""
        criteria.append("Dual_Sim_card" + "=" + req.POST.get("dualsim")) if (req.POST.get("dualsim") != "/") else ""
        criteria.append("Micro_sd" + "=" + req.POST.get("microsd")) if (req.POST.get("microsd") != "/") else ""

        if (req.POST.get("battery") == ">"):
            criteria.append("Battery_Capacity__gte=" + str(current_phone_data[0]['Battery_Capacity'])) if (req.POST.get("battery") != "/") else ""

        if (req.POST.get("ios") or req.POST.get("android") or req.POST.get("bb") or req.POST.get("wp")):
            os_list = []
            if req.POST.get("ios") is not None:
                os_list.append("iOS")
            if req.POST.get("android") is not None:
                os_list.append("Android")
            if req.POST.get("bb") is not None:
                os_list.append("BlackBerry OS")
            if req.POST.get("wp") is not None:
                os_list.append("Windows Phone")
            criteria.append("Operating_System__in="+str(os_list))

        result = None
        filtering = "result = Phone.objects.filter(" + ", ".join(criteria) + ").order_by('-Year')[:3]"
        loc = {}
        exec(filtering, globals(), loc)
        # exec function is not working!
        # result = Phone.objects.filter(Screen_size__gte=0, Dual_Sim_card=True, Operating_System__in=['iOS', 'Android', 'BlackBerry OS', 'Windows Phone'])[:3]
        
        ctx = {
            'accstatus' : req.user.is_authenticated,
            'list' : loc['result'],
            'current' : req.POST.get("model")
        }
        return render(req, 'filterresult.html', ctx)
        
    modeltype = list(Phone.objects.order_by().values_list('Brand').distinct())
    modeltype = [rem[0] for rem in modeltype]
    ctx = {
        "accstatus" : req.user.is_authenticated,
        "modellist" : modeltype
    }
    return render(req, 'filter.html', ctx)

def displayone(req, pid):
    # independent page for showing one phones 
    # get the pid from the url
    try:
        phoneobj = Phone.objects.get(pid = pid)
    except ObjectDoesNotExist:
        return redirect('/')


    if req.method == "POST":
        # only user will create the object
        print("**********")
        print (req.user)
        userobj = Appuser.objects.get(user = req.user)
        r = req.POST.get("rate")
        print (r)
        try:
            tryrate = Rating.objects.get(uid = userobj, pid = phoneobj)
            # already exist, change the record
            tryrate.rate = r
            tryrate.save()
        except:
            # does not exist
            Rating.objects.create(uid = userobj, pid = phoneobj, rate = r)
    #phone object exist

    # crawling youtube related videos list
    rateobj = None
    if req.user.is_authenticated:
        userobj = Appuser.objects.get(user = req.user)
        try:
            rateobj = Rating.objects.get(uid = userobj, pid = phoneobj)
        except:
            pass

    initial = "https://www.youtube.com/results?search_query="
    keyword = phoneobj.Model.replace(" ", "+")
    print ("keyword is " + keyword)
    search = requests.get(initial+keyword+" open box")
    page = search.text
    soup = bs(page, 'html.parser')
    result = soup.findAll('a', attrs={'class':'yt-uix-tile-link'})
    title = soup.findAll('a', attrs={'class': 'ytp-title-link yt-uix-sessionlink'})
    print (title)
    linklist = []
    # con = ssl._create_unverified_context()
    for link in result:
        cur = 'https://www.youtube.com' + link['href']
        title = link["title"]
        vidid = link['href'].split("watch?v=", 1)[1]
        # html = bs(urllib.request.urlopen(cur, context=con))
        linklist.append((cur, vidid, title))

    # get only first 10 results
    linklist = linklist[:10]
    
    # print (linklist)

    # finding the key title
    # first = ['Depth', 'Display_screen', 'Cpu', 'Front_camera_resolution', 'Battery', 'Micro_sd']
    # subtitle = ['Appearance', 'Screen', 'Processing Power', 'Camera', 'Battery', 'Cards']

    ctx = {
        "accstatus" : req.user.is_authenticated,
        "phoneinfo" : phoneobj,
        # crawled list of youtube videos, havent thought of how to display in the individual page NOT DONE!
        "utube" : linklist,
        "rate" : rateobj
    }
    return render(req, "displayphone.html", ctx)

def choosemyphone(req):
    return render(req, "choosemyphone.html", {'accstatus' : req.user.is_authenticated})
