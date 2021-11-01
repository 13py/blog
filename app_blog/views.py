from django.shortcuts import get_list_or_404, redirect
from django.shortcuts import render
from django.views.generic.base import View

from .forms import TagForm, PostForm
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


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        context = {'form': form}
        return render(request, 'app_blog/tag_create.html', context)

    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect(form)
        return render(request, 'app_blog/tag_create.html', context={'form': form})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'app_blog/post_create.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect(form)

        context = {'form': form}
        return render(request, 'app_blog/post_create.html', context)
