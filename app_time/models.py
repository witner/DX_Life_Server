from django.db import models

# Create your models here.
from django.db import models
from app_crm.models import UserInfo
# Create your models here.


class Record(models.Model):
    """
    1、记录当天所作事情记录的时间花费
    """
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField(verbose_name='记录开始日期时间')
    duration = models.IntegerField(verbose_name='记录持续时间', default=0)
    event = models.ForeignKey(verbose_name='记录事件类型', to='Event', to_field='id', on_delete=models.CASCADE)
    remarks = models.CharField(max_length=256, verbose_name='记录备注')
    user = models.ForeignKey(verbose_name='用户', to='app_crm.UserInfo', to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title

    class Meta:
        ordering = ['start_datetime']


class Event(models.Model):
    """
    1 记录事件的类别分类
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='事件类型标题')
    level = models.IntegerField(verbose_name='事件级别', default=1)
    parent_id = models.ForeignKey(to='Event', to_field='id', default=None, blank=True, null=True, on_delete=models.CASCADE)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    color = models.CharField(verbose_name="颜色配置", max_length=7, default="#FFFFFF")
    creator = models.ForeignKey(verbose_name='创建者', to='app_crm.UserInfo', to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
