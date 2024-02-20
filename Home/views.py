from .models import Post, Comment
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def register_user(request):
    if request.method == "POST":
        # register_form = RegisterForm(request.POST or None)
        # if register_form.is_valid():
        username = request.POST.get('username')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        User.objects.create(username=username,
                            first_name=firstname,
                            last_name=lastname,
                            email=email,
                            password=password)
        user = authenticate(username=username, password=password)
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, ("Signed Up successfully."))
        return redirect('/')

    else:
        # register_form = RegisterForm()
        return render(request, 'authenticate/register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, ("Successfully Signed In."))
            return redirect('/')
        else:
            messages.error(request, ("Sign In unsuccessful. Try Again."))
            return redirect('/signin')

    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('index')


def post(request, pk):
    id = pk
    posts = Post.objects.get(id=pk)

    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        name = request.user
        body = request.POST.get('body')
        Comment.objects.create(post=post, name=name, body=body)

        return redirect(f'/posts/{id}')
    else:
        return render(request, 'post.html', {
            'posts': posts,
        })
