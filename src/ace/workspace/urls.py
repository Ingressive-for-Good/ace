from django.contrib import admin
from django.urls import path, include

from .views import (
	welcome, 
	WorkspaceCreateView, 
	UserWorkspaceListView, 
	WorkspaceDetailView,
	WorkspaceUpdateView,
	WorkspaceDeleteView,
	AddContributor,
	ContributorsListView,
	About
	)

urlpatterns = [
    path('', welcome, name='landing_page'),
    path('workspace/new/', WorkspaceCreateView.as_view(), name='create-workspace'),
    path('user/<str:username>/workspaces', UserWorkspaceListView.as_view(), name='user-workspace'),
    path('workspace/<int:pk>/', WorkspaceDetailView.as_view(), name='workspace-details'),
    path('workspace/<int:pk>/update', WorkspaceUpdateView.as_view(), name='workspace-update'),
    path('workspace/<int:pk>/delete', WorkspaceDeleteView.as_view(), name='workspace-delete'),
    path('workspace/<int:pk>/add-contributor/', AddContributor.as_view(), name='add-contributor'),
	path('workspace/<int:pk>/contributors/', ContributorsListView, name='contributors'),
    path('about/', About, name='about'),
]
