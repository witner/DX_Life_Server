#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from app_time.views.done import DoneView
from app_time.views.event import EventView

urlpatterns = [
    path('done/', DoneView.as_view(), name='done'),
    path('event/', EventView.as_view()),
]
