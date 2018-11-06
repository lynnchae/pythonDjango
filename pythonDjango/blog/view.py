# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader, Context
import markdown

__author__ = 'Cailinfeng'

from django.http import HttpResponse, JsonResponse
import time
from pythonDjango.blog.models import TBlog


def index(req):
    static_page = req.get_full_path().split('/')[-1]
    suffix = static_page.split('.')[-1]
    context = {'articles': None, 'myinfo': None, 'nbar': 'index'}
    return render_to_response('blog/home.html', context)


def current_time(request):
    return HttpResponse(time.asctime(time.localtime(time.time())))


def blogs(request):
    blogs = TBlog.objects.filter(user_id=1).values()
    blogs = list(blogs)
    t = loader.get_template("blogs.html")
    c = {'blogs': blogs}
    return HttpResponse(t.render(c))


def blog(request,blogid):
    blog = TBlog.objects.get(id=blogid)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    blog.content = md.convert(blog.content)
    blog.toc = md.toc
    t = loader.get_template("blog.html")
    c = {'blog': blog}
    return HttpResponse(t.render(c))
