from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs_count = Blog.objects.count()
    blogs = Blog.objects.order_by('-created_on')
    context = {
        'blogs': blogs,
        'blogs_count': blogs_count
    }
    return render(request, 'blog/all_blogs.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    # blog = Blog.objects.get(id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context)