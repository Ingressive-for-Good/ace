from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	email = models.EmailField(max_length=255, unique=True)
	profile_pic = models.ImageField(blank=True, null=True)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{ self.user.username }'


