from django import forms
from .models import Announcement


class ApproveForm(forms.Form):
	approve_all = forms.BooleanField(required=False)

class AnnouncementUpdateForm(forms.ModelForm):
	class Meta:
		model = Announcement
		fields = ['title', 'message', 'image']