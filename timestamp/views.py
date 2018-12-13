# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
import calendar
import json

# Create your views here.
def index(request):
    x = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S %Z')
    respons_data = {}
    respons_data['time'] = str(x)

    return JsonResponse(respons_data)

def timestamp(request, date):
    split_date = date.split('-')
    test_date = {}
    try:
        test_date['unix'] = calendar.timegm(datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])).utctimetuple())
        test_date['utc'] = datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])).strftime('%a, %d %b %Y %H:%M:%S %Z')
        #print test_date
        return JsonResponse(test_date)
    except IndexError as inn:
        print inn
        test_date['unix'] = date
        test_date['utc'] = datetime.datetime.utcfromtimestamp(float(date)).strftime('%a, %d %b %Y %H:%M:%S %Z')
        #print test_date
        return JsonResponse(test_date)


def unix_timestamp(request, unix_time):

    test_date = {}
    test_date['unix'] = unix_time
    test_date['utc'] = datetime.datetime.utcfromtimestamp(float(unix_time)).strftime('%a, %d %b %Y %H:%M:%S %Z')
    #print test_date

    return JsonResponse(test_date)

def whoami(request):
    whoiam = {}
    whoiam['ipaddress'] = get_client_ipaddress(request)
    whoiam['software'] = request.META['HTTP_USER_AGENT']
    whoiam['language'] = request.META['HTTP_ACCEPT_LANGUAGE']
    #print whoiam
    return JsonResponse(whoiam)

def get_client_ipaddress(req):

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')
    return ip