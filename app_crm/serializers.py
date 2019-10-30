#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    telephone = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    nickname = serializers.CharField()
    sex = serializers.ChoiceField(choices=UserInfo.SEX_CHOICES)
    age = serializers.IntegerField()
    birthday = serializers.DateField()
    address = serializers.CharField()
    time_create = serializers.DateTimeField()

    def create(self, validated_data):
        return UserInfo.objects.create(**validated_data)


