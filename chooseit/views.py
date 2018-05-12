# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.

def index(req):
    return render(req, 'index.html', {'accstatus' : req.user.is_authenticated})