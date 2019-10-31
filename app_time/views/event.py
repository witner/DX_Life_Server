#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入系统模块

# 第三方模块
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# 导入自定义模块
from app_time.serializers import EventSerializer
from app_time.models import Event
# 设置环境变量


class EventView(APIView):
    def get(self, request):
        """
        请求获取事件信息，
        :param request: 接受请求参数【parent_id、level】
        :return:
        """

        # 获取查询条件
        parent_id = request.query_params.get('parent_id', 0)
        level = request.query_params.get('level', 0)
        try:
            parent_id = int(parent_id)
            level = int(level)
        except Exception:
            content = {'error_msg': '请求参数错误，不能为非数字'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 数据库查询
            event_list = Event.objects.all()
            if parent_id != 0:
                event_list = event_list.filter(parent_id=parent_id)

            if level != 0:
                event_list = event_list.filter(level=level)

            ret = EventSerializer(event_list, many=True)
            return Response(ret.data)






