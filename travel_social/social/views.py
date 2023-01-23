from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.   
def index(request):
    template = 'social/index.html'
    all_posts = Post.objects.all

    context = {
        'all_posts': all_posts,
    }
    return render(request, template, context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.created = timezone.now()
            comment.text = request.POST['text']
            comment.save()
            return redirect('social:detail', post.id)
    else:
        form: CommentForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'social/detail.html', context)

@login_required
def create_post(request):
    template = 'social/post.html'
    form = PostForm(request.POST, request.FILES)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.title = request.POST['title']
            post.dest_type = request.POST['dest_type']
            post.location = request.POST['location']
            post.image = request.FILES['image']
            post.content = request.POST['content']
            post.save()
            return redirect('social:detail', post.id)
    else:
        form: PostForm()

    context = {
        'form': PostForm,
    }
    return render(request, template, context)

def edit_post(request, pk):
    template = 'social/edit.html'
    post = get_object_or_404(Post, pk=pk)   
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(Commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.save()
            return redirect('social:detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
    
    context = {
        'form': PostForm
    }
    return render(request, template, context)

def like_post(request, pk):
    if request.method == 'POST':
        instance = Post.objects.get(pk=pk)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save()
            return render(request, 'social/likes.html', context={'post': instance})
        else:
            instance.likes.remove(request.user)
            instance.save()
            return render(request, 'social/likes.html', context={'post': instance})



