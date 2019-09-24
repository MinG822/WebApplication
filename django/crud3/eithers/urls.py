from django.contrib import admin
from django.urls import path
from . import views

app_name = "eithers"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path()
]