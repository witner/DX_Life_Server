#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views import View


class PublisherView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

