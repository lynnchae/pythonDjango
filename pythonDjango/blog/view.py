# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

from django.core import serializers

__author__ = 'Cailinfeng'

from django.http import HttpResponse, JsonResponse
import time
from pythonDjango.blog.models import TBlog


def index(request):
    return HttpResponse("Hello, world.")


def current_time(request):
    return HttpResponse(time.asctime(time.localtime(time.time())))


def blogs(request):
    blogs = TBlog.objects.filter(user_id=1).values()
    results = list(blogs)
    return JsonResponse(results,safe=False)
