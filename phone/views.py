# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Phone
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
)
# Create your views here.

def displayone(req, pid):
    # independent page for showing one phones 
    # get the pid from the url
    try:
        phoneobj = Phone.objects.get(pid = pid)
    except ObjectDoesNotExist:
        return redirect('/')
    ctx = {
        "accstatus" : req.user.is_authenticated,
        "phoneinfo" : phoneobj
    }
    return render(req, "displayphone.html", ctx)