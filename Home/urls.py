from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.register_user, name="signup"),
    path('signin', views.login_user, name="signin"),
    path('signout', views.logout_user, name="signout"),
    path('posts/<str:pk>', views.post, name="post"),
]
