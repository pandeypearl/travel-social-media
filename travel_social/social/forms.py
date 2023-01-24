from django.forms import ModelForm
from django.db.models import fields
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.TextInput()
    destination = forms.TextInput()
    dest_type = forms.TextInput()
    location = forms.TextInput()
    image = forms.ImageField()
    content = forms.Textarea()
    class Meta:
        model = Post
        fields = (
            'title',
            'destination',
            'dest_type',
            'location',
            'image',
            'content',
        )
        

class CommentForm(forms.ModelForm):
    text = forms.Textarea()
    class Meta:
        model = Comment
        fields = (
            'text',
        ) 
        widgets = {'text': forms.Textarea(attrs={'placeholder': 'comment'})}
        labels = {'text' : ''}