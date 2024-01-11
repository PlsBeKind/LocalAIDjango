from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('play_music/', views.play_music, name='play_music'),
]