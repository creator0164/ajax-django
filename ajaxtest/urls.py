from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.login_index, name='index'),
    path('login/', views.login_view, name='login'),
]
