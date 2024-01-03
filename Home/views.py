from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def register_user(request):
    register_form = RegisterForm()
    if request.method == "POST":
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('index')

    else:
        return render(request, 'authenticate/register.html', {'register_form':register_form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)

        if user is not None:
            login(request, user)
            messages.success(request, ("Successfully Signed In."))
            return redirect('index')
        else:
            messages.error(request, ("Sign In unsuccessful. Try Again."))
            return redirect('signin')
        
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')

def post(request, pk):
    posts = Post.objects.get(id=pk)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            clean_data = comment_form.cleaned_data
            print(clean_data)
            new_comment = comment_form.save(commit=False)
            new_comment.post = Post.objects.get(pk=pk)
            new_comment.save()
        return redirect()

    return render(request, 'post.html', {'posts': posts, 'comment_form': comment_form})
