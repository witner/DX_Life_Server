#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app_test.models import *
from django.http import HttpResponse

def publisher_add(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('publisher_add get')
    return HttpResponse('publisher_add')

def publisher_detail(request):
    return HttpResponse('publisher_detail')

def publisher_delete(request):
    return HttpResponse('publisher_delete')

def author_add(request):
    return HttpResponse('author_add')

def book_add(request):
    return HttpResponse('book_add')
