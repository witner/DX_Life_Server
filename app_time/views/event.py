#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入系统模块

# 第三方模块
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from app_time.views.pagination import StandardResultsSetPagination
# 导入自定义模块
from app_time.models import Event
from app_time.serializers import EventModelSerializer
from app_time.views.filter import EventFilter
# 设置环境变量


class EventModelViewSet(ModelViewSet):
    # 查询集
    queryset = Event.objects.filter(is_delete=False).order_by('id')
    # 序列号
    serializer_class = EventModelSerializer
    # 分页
    pagination_class = StandardResultsSetPagination
    # 过滤
    filterset_class = EventFilter









