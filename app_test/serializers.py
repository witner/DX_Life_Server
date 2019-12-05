#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers


class AuthorSerializers(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=32)


class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

