from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(blank=True, null=True)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{ self.user.username }'


