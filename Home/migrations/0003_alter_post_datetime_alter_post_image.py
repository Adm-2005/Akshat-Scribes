# Generated by Django 4.2.8 on 2023-12-29 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_post_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 19, 19, 18, 864305)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
