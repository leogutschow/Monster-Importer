from django.urls import path
from .views import ForumIndex, ForumCategory
app_name = 'forum'

urlpatterns = [
    path('', ForumIndex.as_view(), name='forum_index'),
    path('<int:id>', ForumCategory.as_view(), name='category'),
]