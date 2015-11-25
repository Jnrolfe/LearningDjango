from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Timer(models.Model):
	start_time = models.PositiveIntegerField(default=0)
	end_time = models.PositiveIntegerField(default=0)
	elapsed_time = models.PositiveIntegerField(default=0)
	running_total = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, unique=True)

	def __str__(self):
		return "Timer instance for %s" % (self.user) 