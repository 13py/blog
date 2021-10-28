from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic.base import View

from .models import Post
from .models import Tag
from .utils import ObjectDetailMixin


class PostsList(View):
    def get(self, request):
        posts = get_list_or_404(Post)
        context = {'posts': posts}
        return render(request, 'app_blog/index.html', context)


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'app_blog/post_detail.html'


class TagsList(View):
    def get(self, request):
        tags = get_list_or_404(Tag.objects.values('title', 'slug'))
        context = {'tags': tags}
        return render(request, 'app_blog/tags_list.html', context)


class TagPostsList(ObjectDetailMixin, View):
    model = Tag
    template = 'app_blog/tag_posts_list.html'
