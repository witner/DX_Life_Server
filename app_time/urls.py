#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
# from app_time.views.done import DoneModelViewSet
from app_time.views.event import EventModelViewSet, EventTreeAPIView
from app_time.views.record import RecordToVueMobileAPIView

urlpatterns = [
    # path('done/list', DoneModelViewSet.as_view({"get": "list", 'post': 'create'})),
    # path('done/retrieve/<int:pk>', DoneModelViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('event/list', EventModelViewSet.as_view({"get": "list", 'post': 'create'})),
    path('event/retrieve/<int:pk>', EventModelViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('event/tree', EventTreeAPIView.as_view()),
    path('record/list/vue_mobile/', RecordToVueMobileAPIView.as_view()),
]
