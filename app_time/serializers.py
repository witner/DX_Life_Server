#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from app_time.models import *
from app_crm.serializers import UserInfoSerializer


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)
    level = serializers.IntegerField()
    # parent_id = serializers.IntegerField()


class DoneSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    start_date = serializers.DateField()
    start_time = serializers.TimeField()
    duration = serializers.IntegerField()
    happiness = serializers.IntegerField()
    health = serializers.IntegerField()
    fulfillment = serializers.IntegerField()
    event = EventSerializer()
    user = UserInfoSerializer()

    # class Meta:
    #     model = Done
    #     fields = '__all__'
