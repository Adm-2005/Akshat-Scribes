from django.contrib import admin
from .models import *

admin.site.register(Post)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('comment_post', 'comment_active')
#     date_hierarchy = 'comment_dt'
