# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

class Appuser(models.Model):
    uid = models.AutoField(
        auto_created = True,
        primary_key = True,
        blank = True,
        verbose_name = "user id",
        help_text = "ID that can uniquely identify user"
    )
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        default = None
    )
    email = models.EmailField(
        default = None,
        verbose_name = "email of user"
    )

    
