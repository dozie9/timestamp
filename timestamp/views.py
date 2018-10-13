# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json

# Create your views here.
def index(request):
    x = datetime.datetime.now()
    respons_data = {}
    respons_data['time'] = str(x)
    print x
    return HttpResponse(json.dumps(respons_data), content_type="application/json")