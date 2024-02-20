from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': '.form',
            'placeholder': 'Email Address',
            'size': 20
        }))
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'First Name',
                                     'size': 20
                                 }))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Last Name',
                                    'size': 20
                                }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
