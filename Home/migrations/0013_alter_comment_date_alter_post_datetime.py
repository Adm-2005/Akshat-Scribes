# Generated by Django 4.2.8 on 2024-01-06 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_rename_name_comment_username_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 6, 16, 1, 58, 372588)),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 6, 16, 1, 58, 372588)),
        ),
    ]