# Generated by Django 4.2.8 on 2024-01-06 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_comments_alter_post_datetime_delete_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 6, 15, 11, 24, 447338)),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 6, 15, 11, 24, 447338)),
        ),
    ]
