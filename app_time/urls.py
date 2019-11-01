#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from app_time.views.done import DoneView, DoneModelViewSet
from app_time.views.event import EventView

urlpatterns = [
    path('done/list', DoneModelViewSet.as_view({"get": "list", 'post': 'create'})),
    path('done/retrieve/<int:pk>', DoneModelViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('done/', DoneView.as_view(), name='done'),
    path('event/', EventView.as_view()),
]
