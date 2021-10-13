from django.contrib import admin
from django.urls import path, include

from .views import welcome

urlpatterns = [
    path('', welcome, name='landing_page'),
]
