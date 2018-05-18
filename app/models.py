# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MarkerModel(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    icon = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
