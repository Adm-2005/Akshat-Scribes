from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    datetime = models.DateTimeField(default=datetime.now())
    content = models.CharField(max_length=10000000)
