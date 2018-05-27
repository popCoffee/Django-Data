# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models

class Customer (models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    area = models.CharField(max_length=32)
    tariff = models.CharField(max_length=32)

class Reading (models.Model):
    customer = models.ForeignKey(Customer)
    timestamp = models.DateTimeField()
    units = models.FloatField()
