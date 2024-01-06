from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': '.form', 'placeholder':'Email Address','size':20}))
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder':'First Name','size':20}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder':'Last Name','size':20}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username','size':20})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password','size':20})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password','size':20})

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('username', 'body')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['username'].widgets.attrs.update({'size':20})
        self.fields['body'].widgets.attrs.update({'placeholder':'Add Comment','size':20})
