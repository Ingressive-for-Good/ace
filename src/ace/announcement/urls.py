from django.urls import path

from .views import create_announcement, delete_announcement


urlpatterns = [
    path('new-announcement', create_announcement, name='new-announcement'),
    path('delete-announcement/<int:pk>', delete_announcement, name='delete-announcement'),
]
