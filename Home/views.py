from .models import Post, Comment
from django.contrib import messages
from .forms import RegisterForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def register_user(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Signed Up successfully."))
            return redirect('index')

    else:
        register_form = RegisterForm()
        return render(request, 'authenticate/register.html',
                      {'register_form': register_form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

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
    # comments = post.comments.filter(active = True)
    # new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.instance.username = request.user
            # new_comment = comment_form.save(commit = False)
            # new_comment.post = posts
            # new_comment.save()
            return redirect('post')
    else:
        comment_form = CommentForm()
        return render(request, 'post.html', {
        'posts': posts,
        'comment_form': comment_form,
        # 'comments' : comments,
        # 'new_comment' : new_comment,
    })
   

    