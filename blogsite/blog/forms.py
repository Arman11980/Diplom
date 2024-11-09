from django import forms
from .models import Post, Comment

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Ваш логин:')
    password = forms.CharField(min_length=8, label='Ваш пароль')
    repeate_password = forms.CharField(min_length=8, label='Повторите ваш пароль')
    age = forms.CharField(max_length=3, label='Ваш возраст')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']