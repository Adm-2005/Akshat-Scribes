from django.urls import path
from . import views

urlpatterns = [
    path('home', views.forum_home, name='forum_home'),
]
