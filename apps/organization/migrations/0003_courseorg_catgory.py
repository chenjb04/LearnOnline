# Generated by Django 2.0.5 on 2018-05-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180515_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='catgory',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default='pxjg', max_length=20, verbose_name='课程类别'),
        ),
    ]
