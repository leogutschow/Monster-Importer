from django.urls import path
from .views import Login, Logout, Register, ProfileView

app_name = 'auth'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('profile/<str:slug>', ProfileView.as_view(), name='profile'),
    path('profile/<str:slug>/monsters', ProfileView.as_view(), name='profile_monsters'),
]
