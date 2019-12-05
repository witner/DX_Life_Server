#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app_test.models import *
from django.http import HttpResponse
from app_test.serializers import AuthorSerializers


def author_detail(request):
    author = Author.objects.get(pk=1)
    serializer = AuthorSerializers(author)
    print(serializer.data)
    return HttpResponse(serializer.data)


def author_list(request):
    authors = Author.objects.all()
    obj_serializer = AuthorSerializers(authors, many=True)
    print(obj_serializer.data)
    return HttpResponse('author_list')










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


