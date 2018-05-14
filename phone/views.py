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

# import ssl
# Create your views here.

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

        # print (req.POST.get("os"))

        filtering = "Phone.objects.filter("
        if (req.POST.get("screen") == ">"):
            filtering += ("Screen_size__gte=" + "0")
        elif (req.POST.get("screen") == "<"):
            filtering += ("Screen_size__lte=" + "0")
        elif (req.POST.get("screen") == "="):
            filtering += ("Screen_size=" + "0")

        filtering += (", Fingerprint_Authentication" + "=" + req.POST.get("fingerprint")) if (req.POST.get("fingerprint") != "/") else ""
        filtering += (", Dual_Sim_card" + "=" + req.POST.get("dualsim")) if (req.POST.get("dualsim") != "/") else ""
        filtering += (", Micro_sd" + "=" + req.POST.get("microsd")) if (req.POST.get("microsd") != "/") else ""
        if (req.POST.get("battery") == ">"):
            filtering += (", Battery_Capacity__gte=" + "0") if (req.POST.get("battery") != "/") else ""
        # filtering += ("Operating_System" + "=" + req.POST.get("os")) if (req.POST.get("os") != "/") else ""
        filtering += ")"

        exec(filtering)
        
        return redirect('/')
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
    if req.user.is_authenticated:
        userobj = Appuser.objects.get(user = req.user)
        try:
            rateobj = Rating.objects.get(uid = userobj, pid = phoneobj)
        except:
            rateobj = None

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
