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
# Create your views here.

def listfunc(req):
    return render(req, "listofphones.html")

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
        print (req.POST.get("screen"))
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

    #phone object exist

    # crawling youtube related videos list
    initial = "https://www.youtube.com/results?search_query="
    keyword = phoneobj.Model.replace(" ", "+")
    print ("keyword is " + keyword)
    search = requests.get(initial+keyword)
    page = search.text
    soup = bs(page, 'html.parser')
    result = soup.findAll('a', attrs={'class':'yt-uix-tile-link'})
    linklist = []
    for link in result:
        cur = 'https://www.youtube.com' + link['href']
        linklist.append(cur)

    print (linklist)

    # finding the key title
    # first = ['Depth', 'Display_screen', 'Cpu', 'Front_camera_resolution', 'Battery', 'Micro_sd']
    # subtitle = ['Appearance', 'Screen', 'Processing Power', 'Camera', 'Battery', 'Cards']

    ctx = {
        "accstatus" : req.user.is_authenticated,
        "phoneinfo" : phoneobj,
        # crawled list of youtube videos, havent thought of how to display in the individual page NOT DONE!
        "utube" : linklist
    }
    return render(req, "displayphone.html", ctx)

def choosemyphone(req):
    return render(req, "choosemyphone.html", {'accstatus' : req.user.is_authenticated})
