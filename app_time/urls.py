#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from app_time.views.done import DoneView

urlpatterns = [
    path('done/', DoneView.as_view(), name='done'),
]
