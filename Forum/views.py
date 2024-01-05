from django.shortcuts import render
from .models import Room, Message


def forum_home(request):
    rooms = Room.objects.all()
    messages = Message.objects.all()
    return render(request, 'forum/forum.html', {
        'rooms': rooms,
        'messages': messages
    })
