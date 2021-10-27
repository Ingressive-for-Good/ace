from django.contrib import admin
from django.urls import path, include

from .views import welcome, WorkspaceCreateView, UserWorkspaceListView, WorkspaceDetailView

urlpatterns = [
    path('', welcome, name='landing_page'),
    path('workspace/new/', WorkspaceCreateView.as_view(), name='create-workspace'),
    path('user/<str:username>/workspaces', UserWorkspaceListView.as_view(), name='user-workspace'),
    path('workspace/<int:pk>/', WorkspaceDetailView.as_view(), name='workspace-details'),

]
