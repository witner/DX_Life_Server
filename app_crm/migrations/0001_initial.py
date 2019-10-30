# Generated by Django 2.2.6 on 2019-10-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('telephone', models.CharField(max_length=20, unique=True, verbose_name='手机号')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='邮箱')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('nickname', models.CharField(blank=True, default='小白', max_length=16, verbose_name='昵称')),
                ('sex', models.CharField(blank=True, choices=[('M', '男性-Male'), ('F', '女性-Female')], default='M', max_length=2, verbose_name='性别')),
                ('age', models.IntegerField(blank=True, default=18, verbose_name='年龄')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('address', models.CharField(blank=True, default='无', max_length=128, verbose_name='地址')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]
