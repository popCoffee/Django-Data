# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Sum
from django.shortcuts import render

from consumption.models import Customer, Reading
from django.db.models.functions import TruncDate
import json

def summary(request):
    #get a query set of dictionaries with keys date(day) and sum
    t = Reading.objects.all().annotate(date=TruncDate('timestamp')).values('date').annotate(units=Sum('units')).values('date', 'units')
    data = {'x': [], 'y': []}
    for each in t:
        data['x'].append(str(each['date']))
        data['y'].append(each['units'])

    #get id area tariff
    latest_question_list = Customer.objects.values('id')
    context = {'latest_question_list': latest_question_list , 'data':json.dumps(data)}
    return render(request, 'consumption/summary.html', context)


def detail(request, customer_id=3000):
    try:
        #get text input id
        orig = request.GET['originaltxt'].lower()
        #convert to integer
        customer_id = int(orig)
    except:
        customer_id = 3000

    #return date and sum
    t_indiv = Reading.objects.filter(customer=customer_id).annotate(date=TruncDate('timestamp')).values('date').annotate(units=Sum('units')).values('date', 'units')
    data_indiv = {'x': [], 'y': []}
    for each in t_indiv:
        data_indiv['x'].append(str(each['date']))
        data_indiv['y'].append(each['units'])

    latest_info_list = Customer.objects.get(id=customer_id)
    context = {'data_indiv':json.dumps(data_indiv), 'latest_info_list': latest_info_list }
    return render(request, 'consumption/detail.html', context)
