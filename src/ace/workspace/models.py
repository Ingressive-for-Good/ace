from account.models import Profile
from django.urls import reverse
import datetime
from django.utils import timezone

# Create your models here.


class Workspace(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	head = models.ForeignKey(User, on_delete= models.CASCADE)
	image = models.ImageField(default='default.jpg', null=True, blank=True)
	contributors = models.ManyToManyField(Profile, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('workspace-details', kwargs={'pk' : self.pk})

	def is_contributor(self):
		return self.contributors.all()


	@property
	def announcements(self):
		return self.announcement_set.all().order_by('-updated_at')
