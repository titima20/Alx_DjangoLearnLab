from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment

class TagWidget(forms.TextInput):
    def format_value(self, value):
        if value is not None and not isinstance(value, str):
            return ', '.join(value)
        return value

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text='Separate tags with commas')
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
