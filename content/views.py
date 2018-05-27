# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Sum
from django.shortcuts import render

from consumption.models import Customer, Reading
from django.db.models.functions import TruncDate


import json
import numpy as np
import pandas as pd

def home(request):
    return render(request, 'consumption/home.html')

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

    tt = Reading.objects.filter(customer=customer_id).annotate(date=TruncDate('timestamp')).values('date').annotate(units=Sum('units')).values('date', 'units')
    data_per_time = []
    for each in tt:
        data_per_time.append(each['units'])
    stddev = np.std(data_per_time)

    #return date and sum
    t_indiv = Reading.objects.filter(customer=customer_id).annotate(date=TruncDate('timestamp')).values('date').annotate(units=Sum('units')).values('date', 'units')
    data_indiv = {'x': [], 'y': []}
    data_var   = {'x': [], 'y': [], 'z': []}

    for each in t_indiv:
        data_indiv['x'].append(str(each['date']))
        data_indiv['y'].append(each['units'])
        data_var['x'].append(str(each['date']))
        data_var['y'].append((each['units'])+stddev)
        data_var['z'].append((each['units'])-stddev)
    #rolling average and standard deviation
    df = pd.DataFrame(data_var)
    df['y'] = df['y'].rolling(window=10).mean()
    df['y'].fillna(df['y'].mean(), inplace = True)
    df['z'] = df['z'].rolling(window=10).mean()
    df['z'].fillna(df['z'].mean(), inplace = True)
    data_var_pos   = {'x': [], 'y': []}
    data_var_neg   = {'x': [], 'y': []}
    data_var_pos['y'] = df['y'].tolist()
    data_var_pos['x'] = df['x'].tolist()
    data_var_neg['y'] = df['z'].tolist()
    data_var_neg['x'] = df['x'].tolist()

    #data_total = [data_indiv, data_var]
    latest_info_list = Customer.objects.get(id=customer_id)
    context = {'data_indiv':json.dumps(data_indiv), 'latest_info_list': latest_info_list, 'data_var':json.dumps(data_var_pos), 'data_var_neg':json.dumps(data_var_neg) }
    return render(request, 'consumption/detail.html', context)
