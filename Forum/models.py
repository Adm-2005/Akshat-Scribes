from django.db import models
from datetime import datetime

class Room(models.Model):
    room_name = models.CharField(max_length = 1000)

class Message(models.Model):
    message_user = models
    message_content = models.CharField(max_length = 100000)
    message_dt = models.DateTimeField(default = datetime.now, blank= True)
    message_room = models.CharField(max_length = 1000)


