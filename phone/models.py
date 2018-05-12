# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def dirtoup(imgobj, filename):
    return '{0}/{1}/{2}'.format(imgobj.Brand, imgobj.Model, filename)
# Create your models here.
class Phone(models.Model):
    pid = models.AutoField(
        auto_created = True,
        primary_key = True,
        verbose_name = "Phone ID"
    )
    Brand = models.CharField(
        default = "No Information",
        max_length = 250,
        blank = True
    )
    Model = models.CharField(
        default = "No Information",
        max_length = 250,
        blank = True
    )
    Year = models.IntegerField(
        blank = True
    )
    # data is stored in form of character, mayne change to numbers?
    Month = models.IntegerField(
        blank = True
    )
    Depth = models.FloatField(
        blank = True
    )
    Height = models.FloatField(
        # cannot be empty
        blank = False
    )
    Width = models.FloatField(
        blank = False
    )
    Weight = models.FloatField(
        blank = True
    )
    Colors = models.CharField(
        default = "No Information",
        max_length = 250,
        blank = True
    )
    Display_screen = models.CharField(
        default = "No Information",
        max_length = 250,
        blank = True
    )
    Screen_size = models.FloatField(
        blank = True
    )
    Screen_ratio = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )
    Screen_to_body_ratio = models.FloatField(
        blank = True
    )
    Screen_ppi = models.IntegerField(
        blank = True
    )
    Screen_resolution_x = models.FloatField(
        blank = True
    )
    Screen_resolution_y = models.FloatField(
        blank = True
    )
    Cpu  = models.CharField(
        max_length = 250,
        blank = True,
        default = "No Information"
    )
    Cpu_specification = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )
    Gpu = models.CharField(
        blank = True,
        default = "No Information",
        max_length = 250
    )
    Ram = models.CharField(
        blank = True,
        default = "No Information",
        max_length = 250
    )
    #character?
    Rom = models.CharField(
        blank = True,
        default = "No Information",
        max_length = 250
    )
    Front_camera_resolution = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )
    Front_camera_aperture = models.CharField(
        blank = True,
        default = "No Information",
        max_length = 250
    )
    Rear_camera_resolution = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )
    Rear_camera_aperture = models.CharField(
        blank = True,
        default = "No Information",
        max_length = 250

    )
    Battery_Capacity = models.IntegerField(
        blank = True
    )
    Removable_Battery = models.BooleanField(
        blank = True
    )
    Micro_sd = models.BooleanField(
        blank = True
    )

    # twog = 
    # threeg
    # fourg

    Sim_card = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )

    Dual_Sim_card = models.BooleanField(
        blank = True

    ) 
    Hybrid_Sim_card = models.BooleanField(
        blank = True

    )

    Radio = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )
    Usb = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )
    WLan = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"

    )
    Gps = models.BooleanField(
        blank = True
    )
    Bluetooth = models.BooleanField(
        blank = True
    )
    NFC = models.BooleanField(
        blank = True
    )
    # jack #whatis this
    Infra_Red = models.BooleanField(
        blank = True
    )
    Operating_System = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )
    Version = models.CharField(
        blank = True,
        max_length = 250,
        default = "No Information"
    )
    Fingerprint_Authentication = models.BooleanField(
        blank = True
    )
    Picture = models.ImageField(
        default = "default.png",
        blank = True,
        upload_to = dirtoup
    )

    def nameit(self):
        return [(attr.name, attr.value_to_string(self)) for attr in Phone._meta.fields]