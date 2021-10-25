from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'app_blog/index.html', context)
