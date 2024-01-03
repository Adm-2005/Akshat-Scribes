from django.shortcuts import render
from .models import *

def forum_home(request):
    return render(request, 'forum.html', {})
