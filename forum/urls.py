from django.urls import path
from .views import ForumIndex, ForumCategory, ForumInside, ForumCreate

app_name = 'forum'

urlpatterns = [
    path('', ForumIndex.as_view(), name='forum_index'),
    path('<str:slug>', ForumCategory.as_view(), name='category'),
    path('<str:slug>/<int:pk>', ForumInside.as_view(), name='forum'),
    path('<str:slug>/create', ForumCreate.as_view(), name='create')
]