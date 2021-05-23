from django.shortcuts import render, get_object_or_404
from . models import Blog

# Create your views here.

def all_home(request):
    Blogs = Blog.objects.all()
    return render(request, 'blog/all_home.html', {'Blogs': Blogs})

def details(request, blog_id):
    Blogs = get_object_or_404(Blog, pk = blog_id)
    return render (request, 'blog/details.html', {'Blog': Blogs })
