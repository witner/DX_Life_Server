from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示字段
    list_display = ['pk', 'name']
    # 分页
    list_per_page = 10
