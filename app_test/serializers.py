#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from app_test.models import *


class AuthorSerializers(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

