#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from app_time.models import *


class DoneSerializer(serializers.Serializer):
    class Meta:
        model = Done
        fields = '__all__'
