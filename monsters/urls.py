from django.urls import path
from .views import MonsterDetail, MonsterList, MonsterCreate

app_name = 'monster'

urlpatterns: list = [
    path('<str:slug>', MonsterDetail.as_view(), name="monster_detail"),
    path('s/', MonsterList.as_view(), name='monster_list'),
    path('new/', MonsterCreate.as_view(), name='monster_create')
]