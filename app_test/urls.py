#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from app_test.views import fbv
from app_test.views import cbv

urlpatterns = [
    # 基本函数的视图
    path('publisher/add', fbv.publisher_add),
    path('publisher/detail', fbv.publisher_detail),
    path('publisher/delete', fbv.publisher_delete),
    path('author/add', fbv.author_add),
    path('author/list', fbv.author_add),
    path('book/add', fbv.book_add),
    # 基于类的视图
    path('publisher/list', cbv.PublisherView.as_view()),
]
