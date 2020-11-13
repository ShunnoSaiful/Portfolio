from django.urls import path, include
from django.contrib import admin

from .views import home

app_name = 'myinfo'
urlpatterns = [
    path('', home, name='home'),
]