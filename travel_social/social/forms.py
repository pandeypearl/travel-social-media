from django.forms import ModelForm
from django import forms
from .models import Post

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