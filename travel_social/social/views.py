from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.utils import timezone

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
    return render(request, 'social/detail.html', {'post': post})

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
