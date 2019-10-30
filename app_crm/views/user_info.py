#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入系统模块
from io import BytesIO
import random
import re
import os
# 第三方模块
from rest_framework.views import APIView
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
# settings.configure()
from django.shortcuts import render, HttpResponse, redirect


def get_pic_code(request):
    """
    获取验证码
    :param request:
    :return: 返回图片流
    """
    if request.method == 'GET':
        text_num = 4        # 验证码字符个数
        text_size = 20      # 验证码字符大小
        pic_width = request.GET.get('pic_width', 150)
        pic_height = request.GET.get('pic_height', 26)

        img = Image.new('RGB', (pic_width, pic_height), color='white')
        draw = ImageDraw.Draw(img)
        # ttf_file_path = os.path.join(settings.BASE_DIR, 'app_c_rbac/static/ttf/经典行书简.TTF'),
        font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'app_crm/static/ttf/经典行书简.TTF'), size=text_size)

        f = BytesIO()

        # 生成验证码
        str_pic_code = ''
        for i in range(text_num):
            # 随机数
            num = random.randint(0, 9)
            lowercase = chr(random.randint(97, 122))  # 取小写字母
            uppercase = chr(random.randint(65, 90))  # 取大写字母
            character = str(random.choice([num, lowercase, uppercase]))  # 从数字，小写字母，大写字母随机选择一个

            x = random.randint(i * int(pic_width / text_num), (i + 1) * int(pic_width / text_num) - text_size)
            y = random.randint(0, int(pic_height - text_size))
            # print(i)
            str_pic_code += character
            draw.text((x, y), character, 'black', font=font)

            # 生成干扰线
            x1 = random.randint(0, pic_width)
            x2 = random.randint(0, pic_width)
            y1 = random.randint(0, pic_height)
            y2 = random.randint(0, pic_height)
            draw.line((x1, y1, x2, y2), fill='black')

        img.save(f, 'png')
        data = f.getvalue()
        # 验证码用session保存
        request.session['str_pic_code'] = str_pic_code

        return HttpResponse(data)


class UserLogin(APIView):
    """
    用户登录
    """
    def get(self, request):
        """
        get 请求登录页面
        :param request:
        :return:
        """
        pass


