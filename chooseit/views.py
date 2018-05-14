    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.db.models import Q
from phone.models import Phone
from rating.models import Rating

# Create your views here.

def index(req):
    if req.method == "POST":
        keyword = req.POST.get('searchkeyword')
        # get all the attribute names
        # attr = [obj.name for obj in Phone._meta.get_fields()] 
        # ty = [Phone._meta.get_field(name).get_internal_type for name in attr]
        # print (ty)
        result = Phone.objects.filter(Q(Model__icontains = keyword))
        ctx = {
            'accstatus' : req.user.is_authenticated,
            'list' : result,
            'keyword' : keyword
        }
        return render(req, 'listofphones.html', ctx)

    rating_table = {}
    rating_data = Rating.objects.all()
    for data in rating_data.values_list():
        uid, pid, rate = data[1]-1, data[2]-1, data[3]
        if rating_table.get(pid, "empty"):
            rating_table[pid] = []
        rating_table[pid].append(rate)
    
    avg_score = {}
    for i in rating_table:
        avg_score[i] = (sum(rating_table[i])/len(rating_table[i]))

    top_score = [i[0] for i in sorted(avg_score.items(), key=lambda x: -x[1])[:5]]
    phoneobj = Phone.objects.filter(pid__in = top_score)

    return render(req, 'index.html', {'accstatus' : req.user.is_authenticated, 'name' : req.user.username, "phoneinfo" : phoneobj})