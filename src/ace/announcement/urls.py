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
	path('announcement/<int:pk>/', AnnouncementListView.as_view(), name='announcements'),
	path('new-announcement/<int:pk>/', AnnouncementCreateView.as_view(), name='new-announcement'),
	path('announcement/<int:pk>/',AnnouncementDetailView.as_view(), name='announcement-details'),
	path('announcement/<int:pk>/update', AnnouncementUpdateView.as_view(), name='announcement-update'),
	path('delete-announcement/<int:pk>', AnnouncementDeleteView.as_view(), name='delete-announcement'),
]
