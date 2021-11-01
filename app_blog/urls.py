from django.urls import path

from .views import PostCreate
from .views import PostDetail, TagCreate
from .views import PostsList
from .views import TagPostsList
from .views import TagsList

urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', TagsList.as_view(), name='tags'),
    path('tag/create/', TagCreate.as_view(), name='tag_create'),
    path('tag/<slug:slug>', TagPostsList.as_view(), name='tag'),
]
