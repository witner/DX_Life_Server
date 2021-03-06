# Generated by Django 2.2.6 on 2019-12-03 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='事件类型标题')),
                ('level', models.IntegerField(default=1, verbose_name='事件级别')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.UserInfo', verbose_name='创建者')),
                ('parent_id', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_time.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_datetime', models.DateTimeField(verbose_name='记录开始日期时间')),
                ('duration', models.IntegerField(default=0, verbose_name='记录持续时间')),
                ('remarks', models.CharField(max_length=256, verbose_name='记录备注')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_time.Event', verbose_name='记录事件类型')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.UserInfo', verbose_name='用户')),
            ],
            options={
                'ordering': ['start_datetime'],
            },
        ),
    ]
