#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination

# class MyPagination(PageNumberPagination):
#     page_size = 1

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
