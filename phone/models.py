# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class phone(models.Model):
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
        default = "No Information"
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
        blank = True
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
        blank = True
    )
    Cpu_specification = models.CharField(
        blank = True,
        default = "No Information"
    )
    Gpu = models.CharField(
        blank = True,
        default = "No Information"
    )
    Ram = models.CharField(
        blank = True,
        default = "No Information"
    )
    #character?
    Rom = models.CharField(
        blank = True,
        default = "No Information"
    )
    Camfront = models.FloatField(
        blank = False
    )
    Camfrontape = models.CharField(
        blank = True,
        default = "No Information"
    )
    Camrear = models.FloatField(
        blank = True
    )
    Camrearape = models.CharField(
        blank = True,
        default = "No Information"

    )
    Batcapacity = models.IntegerField(
        blank = True
    )
    Batremovable = models.BooleanField(
        blank = True
    )
    Radio = models.CharField(
        blank = True,
        default = "No Information"
    )
    Usb = models.CharField(
        blank = True,
        default = "No Information"
    )
    Micro_sd = models.BooleanField(
        blank = True
    )

    # twog = 
    # threeg
    # fourg

    Sim_card = models.CharField(
        blank = True,
        default = "No Information"
    )

    Dual_Sim_card = models.BooleanField(
        blank = True

    ) 
    Hybrid_Sim_card = models.BooleanField(
        blank = True

    )
    WLan = models.CharField(
        blank = True,
        default = "No Information"

    )
    Gps = models.BooleanField(
        blank = True
    )
    Bluetooth = models.CharField(
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
        default = "No Information"
    )
    Version = models.CharField(
        blank = True,
        default = "No Information"
    )
    Fingerprint_Authentication = models.BooleanField(
        blank = True
    )