from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Post
from .models import Tag


def posts_list(request):
    posts = get_list_or_404(Post)
    context = {'posts': posts}
    return render(request, 'app_blog/index.html', context)


def post_detail(request, slug):
    # post = Post.objects.values('title', 'text').get(slug=slug)
    post = get_object_or_404(Post.objects.values('title', 'text'), slug=slug)
    context = {'post': post}
    return render(request, 'app_blog/post_detail.html', context)


def tags_list(request):
    tags = get_list_or_404(Tag.objects.values('title', 'slug'))
    context = {'tags': tags}
    return render(request, 'app_blog/tags_list.html', context)


def tag_detail(request, slug):
    # posts = Tag.objects.get(slug=slug)
    # .prefetch_related('posts').
    posts = Tag.objects.prefetch_related('posts').get(slug__iexact=slug)
    # posts = Tag.objects.prefetch_related(
    #     Prefetch(
    #         'posts',
    #         queryset=Post.objects.filter(slug=slug),
    #         to_attr="title_posts",
    #     )
    # )
    # print(posts[1].posts.all())
    context = {'posts': posts}
    return render(request, 'app_blog/tag_posts_list.html', context)
