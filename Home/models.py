from django.db import models
from datetime import datetime
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    datetime = models.DateTimeField(default=datetime.now())
    content = models.CharField(max_length=10000000)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length = 500)
    comment_dt = models.DateField(default = datetime.now, blank=True)
    comment_active = models.BooleanField(default=True)

    