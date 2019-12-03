from django.contrib import admin
from app_crm.models import UserInfo
# Register your models here.


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示字段
    list_display = ['id', 'username', 'telephone', 'email', 'nickname']
    # 过滤条件
    list_filter = ['username']
    # 搜索字段
    search_fields = ['username']
    # 分页
    list_per_page = 10
