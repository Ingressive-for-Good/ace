from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from workspace.models import Workspace

# Create your models here.

class Chat(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	workspace = models.ForeignKey(Workspace, on_delete= models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)
	content = models.TextField()




