#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入系统模块
# 第三方模块
from rest_framework import serializers
# 导入自定义模块
from app_time.models import *
from app_crm.serializers import UserInfoModelSerializer


class EventSerializer(serializers.Serializer):
    """
    使用自定义方式定义序列器，自己定义每一个序列化和反序列化的字段
    """
    # 只读序列器read_only
    id = serializers.IntegerField(read_only=True)
    # id 只在序列化使用，故使用read_only
    title = serializers.CharField(max_length=32)
    # title 序列化和反序列化都使用，故不使用其他参数
    level = serializers.IntegerField()
    parent_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # parent_id 只在序列化使用
    parent_id_w = serializers.IntegerField(write_only=True)
    # parent_id_w 只在反序列化使用，故使用故使用write_only
    color = serializers.CharField(max_length=6)

    def create(self, validated_data):
        """
        添加Event
        :param validated_data:
        :return:
        """
        obj = Event.objects.create(title=validated_data['title'],
                                   level=validated_data['level'],
                                   parent_id_id=validated_data['parent_id_w'],
                                   color=validated_data['color'])
        return obj

    def update(self, instance, validated_data):
        """
        修改Event
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title', instance.title)
        instance.level = validated_data.get('level', instance.level)
        instance.parent_id = validated_data.get('parent_id_w', instance.parent_id)
        instance.color = validated_data.get('color', instance.color)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()
        return instance




# class EventModelSerializer(serializers.ModelSerializer):
#     """
#     遇到问题：通过model方式定义serializers,解决自己指向自己的问题，通过depth深度控制显示父级
#     """
#     # 创建者
#     # creator = UserInfoModelSerializer()
#
#     class Meta:
#         model = Event
#         fields = ('id', 'title', 'level', 'parent_id', 'is_delete', 'creator')
#         depth = 1
#
#     def create(self, validated_data):
#         return Event.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.level = validated_data.get('level', instance.level)
#         instance.parent_id = validated_data.get('parent_id', instance.parent_id)
#         instance.is_delete = validated_data.get('is_delete', instance.is_delete)
#         instance.save()
#         return instance





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

