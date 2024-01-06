from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    datetime = models.DateTimeField(default=datetime.now())
    content = models.CharField(max_length=10000000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = models.CASCADE)
    username = models.ForeignKey(User, editable = False, on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)