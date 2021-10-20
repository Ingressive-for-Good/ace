from django.urls import path

from .views import create_announcement


urlpatterns = [
    path('new-announcement', create_announcement, name='new-announcement'),
]
