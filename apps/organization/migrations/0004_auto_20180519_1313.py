# Generated by Django 2.0.5 on 2018-05-19 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_courseorg_catgory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='catgory',
            new_name='category',
        ),
    ]
