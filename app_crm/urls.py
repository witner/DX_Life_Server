#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第三方模块
from django.urls import path
from .views.user_info import get_pic_code
# 导入自定义模块

# 设置环境变量

urlpatterns = [
    # 登录、注销、注册
    # path('user/login/', UserLogin.as_view(), name='user_login'),
    path('user/login/get_pic_code/', get_pic_code, name='user_login'),
]
