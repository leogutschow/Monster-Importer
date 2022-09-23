from django.urls import path
from .views import ForumIndex
app_name = 'forum'

urlpatterns = [
    path('', ForumIndex.as_view(), name='forum_index')
]