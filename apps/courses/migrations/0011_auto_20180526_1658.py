# Generated by Django 2.0.5 on 2018-05-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20180524_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='访问地址'),
        ),
    ]
