# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bs4 import BeautifulSoup as bs

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
# Create your views here.

initial = "https://www.youtube.com/results?search_query="

def displayone(req, pid):
    # independent page for showing one phones 
    # get the pid from the url
    try:
        phoneobj = Phone.objects.get(pid = pid)
    except ObjectDoesNotExist:
        return redirect('/')

    #phone object exist

    # crawling youtube related videos list
    keyword = phoneobj.Model.replace(" ", "+")
    print "keyword is " + keyword
    search = requests.get(initial+keyword)
    page = search.text
    soup = bs(page, 'html.parser')
    result = soup.findAll('a', attrs={'class':'yt-uix-tile-link'})
    linklist = []
    for link in result:
        cur = 'https://www.youtube.com' + link['href']
        linklist.append(cur)

    print linklist

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
