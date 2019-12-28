from django.contrib import admin
from app_time.models import *
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示字段
    list_display = ['id', 'title', 'level', 'parent_id', 'color', 'creator']
    # 过滤条件
    list_filter = ['title']
    # 搜索字段
    search_fields = ['title']
    # 分页
    list_per_page = 10


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示字段
    list_display = ['id', 'start_datetime', 'duration', 'event', 'remarks', 'user']
    # 过滤条件
    list_filter = ['id']
    # 搜索字段
    search_fields = ['id']
    # 分页
    list_per_page = 10

