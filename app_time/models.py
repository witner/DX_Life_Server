from django.db import models

# Create your models here.
from django.db import models
from app_crm.models import UserInfo
# Create your models here.


class Done(models.Model):
    """
    1、记录当天所作事情情况，包括花费时间，幸福、成就、健康度
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, verbose_name='事情标题')
    start_date = models.DateField(verbose_name='开始日期')
    start_time = models.TimeField(verbose_name='开始时间')
    duration = models.IntegerField(verbose_name='持续时间', default=0)
    happiness = models.IntegerField(verbose_name='幸福度', default=0)
    health = models.IntegerField(verbose_name='健康值', default=0)
    fulfillment = models.IntegerField(verbose_name='成就感', default=0)
    event = models.ForeignKey(verbose_name='事件类型', to='Event', to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='用户', to='app_crm.UserInfo', to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    1 记录事件的类别分类
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='事件类型标题')
    level = models.IntegerField(verbose_name='事件级别', default=1)
    parent_id = models.ForeignKey(to='Event', to_field='id', default=0, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
