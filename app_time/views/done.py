#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入系统模块

# 第三方模块
from rest_framework.viewsets import ModelViewSet
from app_time.views.pagination import StandardResultsSetPagination
# 导入自定义模块
from app_time.serializers import DoneSerializer
from app_time.models import Done
from app_time.views.filter import DoneFilter
# 设置环境变量


class DoneModelViewSet(ModelViewSet):
    # 查询集
    queryset = Done.objects.all().order_by('start_time')
    # 序列号
    serializer_class = DoneSerializer
    # 分页
    pagination_class = StandardResultsSetPagination
    # 过滤
    filterset_class = DoneFilter

    # 分页效果实现步骤
    # 第一步、实例化分页器对象
    # page_obj = PageNumberPagination()
    # 第二步、调用分页方法分页queryset
    # page_queryset = page_obj.paginate_queryset(queryset, request, view=self)


