from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    用户信息表
    1、存放用户的基本信息
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=20, unique=True)
    # 手机号
    telephone = models.CharField(verbose_name='手机号', max_length=20, unique=True)
    # 邮箱
    email = models.EmailField(verbose_name='邮箱', max_length=128, unique=True)
    # 密码
    password = models.CharField(verbose_name='密码', max_length=20)
    # 昵称
    nickname = models.CharField(verbose_name='昵称', max_length=16, blank=True, default=u'小白')
    # 性别
    SEX_CHOICES = (
        (u'M', u"男性-Male"),
        (u'F', u"女性-Female"),
    )
    sex = models.CharField(verbose_name="性别", max_length=2, choices=SEX_CHOICES, blank=True, default=u'M')
    # 年龄
    age = models.IntegerField(verbose_name="年龄", blank=True, default=18)
    # 生日
    birthday = models.DateField(verbose_name=u'生日', blank=True, null=True)
    # 地址
    address = models.CharField(verbose_name=u'地址', max_length=128, blank=True, default=u'无')
    # 头像
    # avatar = models.FileField(verbose_name='头像', upload_to='avatars/', default='avatars/default.png')

    # 创建时间
    time_create = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    # # 用户对应角色
    # role = models.ManyToManyField(verbose_name='用户对应角色', to='Role', through='UserToRole',
    #                               through_fields=('user', 'role'), blank=True)
