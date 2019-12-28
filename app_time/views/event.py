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
from app_time.serializers import EventSerializer, EventTreeSerializer
from app_time.views.filter import EventFilter
# 设置环境变量


class EventModelViewSet(ModelViewSet):
    # 查询集
    queryset = Event.objects.filter(is_delete=False).order_by('id')
    # 序列号
    serializer_class = EventSerializer
    # 分页
    pagination_class = StandardResultsSetPagination
    # 过滤
    filterset_class = EventFilter


class EventTreeAPIView(APIView):
    """
    根据父子关系，返回事件列表，数据结构如下:
    eventList: [
          {
            id: 1,
            title: "工作",
            sonEventList: [
              { id: 11, title: "会议" },
              { id: 12, title: "执行" }
            ]
          },
          {
            id: 2,
            title: "学习",
            sonEventList: [
              { id: 21, title: "会议" },
              { id: 22, title: "执行" }
            ]
          }
        ]
    """
    def get(self, request):
        event_list = Event.objects.filter(level=1)
        n_event_list = []

        for event in event_list:
            n_event_dict = {
                'id': event.id,
                'title': event.title,
                'level': event.level,
                'color': event.color,
                'son_event_list': Event.objects.filter(parent_id=event)
            }
            n_event_list.append(n_event_dict)

        s = EventTreeSerializer(n_event_list, many=True)
        print(s.data)
        return Response(s.data)
