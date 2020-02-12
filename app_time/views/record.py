#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入系统模块
import datetime
# 第三方模块
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app_time.views.pagination import StandardResultsSetPagination
# 导入自定义模块
from app_time.models import Record
from app_time.views.filter import RecordFilter
from app_time.serializers import RecordSerializer, RecordSerializerToVueMobile
# 设置环境变量


class RecordModelViewSet(ModelViewSet):
    # 查询集
    queryset = Record.objects.all().order_by('start_time')
    # 序列号
    serializer_class = RecordSerializer
    # 分页
    pagination_class = StandardResultsSetPagination
    # 过滤
    filterset_class = RecordFilter

    # 分页效果实现步骤
    # 第一步、实例化分页器对象
    # page_obj = PageNumberPagination()
    # 第二步、调用分页方法分页queryset
    # page_queryset = page_obj.paginate_queryset(queryset, request, view=self)


class RecordToVueMobileAPIView(APIView):
    def get(self, request):
        r_date = request.query_params.get('date', datetime.date.today())
        print(request.query_params)
        record_obj = Record.objects.get(id=1)
        r = {
            "num": 1,
            "start_date": "2020-01-01",
            "record": record_obj
        }
        s = RecordSerializerToVueMobile(r)
        return Response(s.data)
