from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.base import View

from .models import Post
from .models import Tag


class PostsList(View):
    def get(self, request):
        posts = get_list_or_404(Post)
        context = {'posts': posts}
        return render(request, 'app_blog/index.html', context)


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(
            Post.objects.values('title', 'text'),
            slug__iexact=slug
        )
        context = {'post': post}
        return render(request, 'app_blog/post_detail.html', context)


class TagsList(View):
    def get(self, request):
        tags = get_list_or_404(Tag.objects.values('title', 'slug'))
        context = {'tags': tags}
        return render(request, 'app_blog/tags_list.html', context)


class TagPostsList(View):
    def get(self, request, slug):
        posts = get_object_or_404(Tag, slug=slug)
        context = {'posts': posts}
        return render(request, 'app_blog/tag_posts_list.html', context)
