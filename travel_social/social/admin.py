from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    model = Post
    fields = [
        'user',
        'created',
        'title',
        'destination',
        'dest_type',
        'location',
        'image',
        'content',
        'likes'
    ]

admin.site.register(Post)
admin.site.register(Comment)

