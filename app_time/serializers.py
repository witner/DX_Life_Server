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


class EventTreeSerializer(serializers.Serializer):
    """
    事件树关系序列器，
    """
    # 只读序列器read_only
    id = serializers.IntegerField(read_only=True)
    # id 只在序列化使用，故使用read_only
    title = serializers.CharField(read_only=True, max_length=32)
    # title 序列化和反序列化都使用，故不使用其他参数
    level = serializers.IntegerField(read_only=True)
    color = serializers.CharField(max_length=6, read_only=True)
    son_event_list = EventSerializer(read_only=True, many=True)


class RecordSerializer(serializers.ModelSerializer):
    """
    默认的Record数据结构，与models对应
    """
    event = EventSerializer(read_only=True)

    class Meta:
        model = Record
        fields = ('id', 'start_datetime', 'duration', 'event', 'remarks', 'user')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('start_datetime', instance.title)
    #     instance.level = validated_data.get('duration', instance.level)
    #     instance.parent_id = validated_data.get('parent_id', instance.parent_id)
    #     instance.is_delete = validated_data.get('is_delete', instance.is_delete)
    #     instance.save()
    #     return instance


class RecordSerializerToVueMobile(serializers.Serializer):
    """
    给VueMobile移动前端的记录数据结构
    """
    num = serializers.IntegerField(read_only=True)
    start_date = serializers.DateField(read_only=True)
    record = RecordSerializer(read_only=True)
    pass



