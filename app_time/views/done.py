#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入系统模块

# 第三方模块
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# 导入自定义模块
from app_time.serializers import DoneSerializer
from app_time.models import Done
# 设置环境变量


class DoneView(APIView):
    def get(self, request):
        # 取单个数据
        done_obj = Done.objects.first()
        ret = DoneSerializer(done_obj)
        # 取多个数据
        done_list = Done.objects.all()
        ret = DoneSerializer(done_list, many=True)
        return Response(ret.data)
        pass

    def post(self, request):
        """
        添加数据
        :param request:
        :return:
        """
        serializer_obj = DoneSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.validated_data)
        else:
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
