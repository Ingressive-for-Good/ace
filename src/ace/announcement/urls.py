from django.urls import path

from .views import (
	AnnouncementListView,
	AnnouncementCreateView,
	AnnouncementDetailView,
	AnnouncementUpdateView,
	AnnouncementDeleteView,
	Approve,
	Unapprove
)

urlpatterns = [
	path('approve/<int:pk>/<int:a_pk>/', Approve, name='approve'),
	path('unapprove/<int:pk>/<int:a_pk>/', Unapprove, name='unapprove'),
	path('annoucement/<int:pk>/', AnnouncementListView.as_view(), name='announcements'),
	path('new-announcement/<int:pk>/', AnnouncementCreateView.as_view(), name='new-announcement'),
	path('message/<int:pk>/',AnnouncementDetailView.as_view(), name='message-details'),
	path('message/<int:pk>/update', AnnouncementUpdateView.as_view(), name='message-update'),
	path('delete-announcement/<int:pk>', AnnouncementDeleteView.as_view(), name='delete-announcement'),
]
