#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *


class UserInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        return UserInfo.objects.create(**validated_data)





