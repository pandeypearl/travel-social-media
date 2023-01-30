from django.shortcuts import render
from social.models import Post
from django.db.models import Q

# Create your views here.
def landing(request):
    template = 'landing/index.html'
    

    query = request.GET.get("q")

    if query:
        posts = Post.objects.filter(
            Q(destination__icontains=query) |     
            Q(dest_type__icontains=query) |
            Q(location__icontains=query)
        )
    
    else:
        posts = Post.objects.all

    context = {
        'posts': posts,
        'query': query,
    }

    return render(request, template, context)