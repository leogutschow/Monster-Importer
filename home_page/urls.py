from django.urls import path
from .views import Index, About

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='home_page'),
    path('/about', About.as_view(), name='about')
]