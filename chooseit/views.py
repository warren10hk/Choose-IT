# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.db.models import Q
from phone.models import Phone
# Create your views here.

def index(req):
    if req.method == "POST":
        keyword = req.POST.get('searchkeyword')
        # get all the attribute names
        result = Phone.objects.filter(Q(Model__icontains = keyword))
        ctx = {
            'accstatus' : req.user.is_authenticated,
            'list' : result
        }
        return render(req, 'listofphones.html', ctx)


    return render(req, 'index.html', {'accstatus' : req.user.is_authenticated})