# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from appuser.models import Appuser
from phone.models import Phone

# Create your models here.

class Rating(models.Model):
    uid = models.ForeignKey(
        Appuser,
        to_field = "uid",
        on_delete = models.PROTECT
    )
    pid = models.ForeignKey(
        Phone,
        to_field = "pid",
        on_delete = models.PROTECT
    )
    rate = models.IntegerField(
        default = 1
    )
