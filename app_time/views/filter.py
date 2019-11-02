#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters
from app_time.models import *


class DoneFilter(filters.FilterSet):
    # start_date = filters.DateFilter(field_name='start_date', )
    class Meta:
        model = Done
        fields = ['start_date']


class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        fields = ['id', 'level', 'parent_id']
