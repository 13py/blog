from django.shortcuts import render, get_object_or_404

from .models import Post
from .models import Tag


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'app_blog/index.html', context)


def post_detail(request, slug):
    # post = Post.objects.values('title', 'text').get(slug=slug)
    post = get_object_or_404(Post.objects.values('title', 'text'), slug=slug)
    context = {'post': post}
    return render(request, 'app_blog/post_detail.html', context)


def tags_list(request):
    tags = Tag.objects.values('title', 'slug')
    context = {'tags': tags}
    return render(request, 'app_blog/tags_list.html', context)
