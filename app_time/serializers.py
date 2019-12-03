#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from app_time.models import *
from app_crm.serializers import UserInfoSerializer


class EventSerializer(serializers.ModelSerializer):
    """
    遇到问题：通过model方式定义serializers,解决自己指向自己的问题，通过depth深度控制显示父级
    """
    class Meta:
        model = Event
        fields = ('id', 'title', 'level', 'parent_id')
        depth = 1

    # id = serializers.IntegerField(required=False, read_only=True)
    # title = serializers.CharField(max_length=32)
    # level = serializers.IntegerField()
    # # parent_id = serializers.IntegerField()
    # # parent_id = serializers.

    def create(self, validated_data):
        obj = Event.objects.create(title=validated_data['title'],
                                   level=validated_data['level'],
                                   parent_id_id=validated_data['parent_id'])
        return obj


# class DoneSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False, read_only=True)
#     title = serializers.CharField(max_length=128)
#     start_date = serializers.DateField()
#     start_time = serializers.TimeField()
#     duration = serializers.IntegerField()
#     happiness = serializers.IntegerField()
#     health = serializers.IntegerField()
#     fulfillment = serializers.IntegerField()
#     event = EventSerializer(read_only=True)
#     # 设置反序列字段
#     event_id = serializers.IntegerField(write_only=True)
#     user = UserInfoSerializer(read_only=True)
#     user_id = serializers.IntegerField(write_only=True)
#
#     # class Meta:
#     #     model = Done
#     #     fields = '__all__'
#
#     def create(self, validated_data):
#         done_obj = Done.objects.create(title=validated_data['title'],
#                                        start_date=validated_data['start_date'],
#                                        start_time=validated_data['start_time'],
#                                        duration=validated_data['duration'],
#                                        happiness=validated_data['happiness'],
#                                        health=validated_data['health'],
#                                        fulfillment=validated_data['fulfillment'],
#                                        event_id=validated_data['event_id'],
#                                        user_id=validated_data['user_id'])
#         return done_obj

