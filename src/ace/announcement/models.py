from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from account.models import Profile
from django.urls import reverse
import datetime
from workspace.models import Workspace
from ckeditor.fields import RichTextField

# Create your models here.


class Announcement(models.Model):
	"""model for Announcement"""
	# slug = models.SlugField(unique=True, null=False)
	title = models.CharField(max_length=150 )
	content = RichTextField(max_length=10000)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	expiry_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=1))
	author = models.ForeignKey(Profile, on_delete= models.CASCADE)
	announced = models.BooleanField(default=False)
	approved = models.BooleanField(default=False)
	image = models.ImageField(default='defaulst.png', null=True, blank=True)
	workspace = models.ForeignKey(Workspace, on_delete= models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('announcements', kwargs={'pk': self.workspace.pk })

	def expiry_dates(self):
		data = self.expiry_date - timezone.now()
		return data.days








