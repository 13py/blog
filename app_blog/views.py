from django.shortcuts import render, get_object_or_404

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'app_blog/index.html', context)


def post_detail(request, slug):
    # post = Post.objects.values('title', 'text').get(slug=slug)
    post = get_object_or_404(Post.objects.values('title', 'text'), slug=slug)
    context = {'post': post}
    return render(request, 'app_blog/post_detail.html', context)
