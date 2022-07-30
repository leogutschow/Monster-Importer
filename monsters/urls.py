from django.urls import path
from .views import MonsterDetail

urlpatterns: list = [
    path('<str:slug>', MonsterDetail.as_view())
]