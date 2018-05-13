# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import registerform, loginform
from .models import Appuser
# Create your views here.

def logoutfunc(req):
    print("in logout")
    print (req.user.is_authenticated)
    logout(req)
    return redirect('/')

def loginfunc(req):
    print("in login")
    print (req.user.is_authenticated)
    if req.method == "POST":
        form = loginform(req.POST)
        if form.is_valid():
            usr = form.cleaned_data.get('Username')
            pw = form.cleaned_data.get('Password')
            print (usr, pw)
            log = authenticate(username = usr, password = pw)
            if log:
                login(req, log)
                return redirect('/')
    else: 
        form = loginform()
    
    ctx = {
        'accstatus' : req.user.is_authenticated,
        'form' : form
    } 
    return render(req, 'login.html', ctx)

def register(req):
    if req.method == "POST":
    #  received form submission from user
        form = registerform(req.POST)
        if form.is_valid():
            form.save()
            # u = form.save(commit = False)
            usr = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            mail = form.cleaned_data.get('Email')
            print (usr, pw, mail)
            log = authenticate(username = usr, password = pw)
            print (log)
            user = Appuser.objects.create(user = log, email = mail)
            login(req, log)
            # u.save()
            # redirect to homepage
            return redirect('/')
    else:
        # form is not yet generated 
        form = registerform()
    
    ctx = {
        'accstatus' : req.user.is_authenticated,
        'form' : form,
    }
    return render(req, 'usrapply.html', ctx)
