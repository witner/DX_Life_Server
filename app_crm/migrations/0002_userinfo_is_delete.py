# Generated by Django 2.2.6 on 2019-12-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]