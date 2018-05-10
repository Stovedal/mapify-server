# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class MarkerModel(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    icon = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
