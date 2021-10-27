from django.urls import path

from .views import post_detail
from .views import posts_list
from .views import tag_detail
from .views import tags_list

urlpatterns = [
    path('', posts_list, name='posts'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('tags/', tags_list, name='tags'),
    path('tag/<slug:slug>', tag_detail, name='tag'),
]
