from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': '.form', 'placeholder':'Email Address','size':30}))
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder':'First Name','size':30}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder':'Last Name','size':30}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username','size':30})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password','size':30})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password','size':30})

class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=100000, widget=forms.Textarea(attrs={'placeholder':'Add Comment', 'size':100, 'border-radius':'8px'}))
    class Meta:
        model = Comment
        fields = ('comment',)
