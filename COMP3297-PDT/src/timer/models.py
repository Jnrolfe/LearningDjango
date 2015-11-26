from django.db import models
from django.contrib.auth.models import User
from project.models import Iteration

# Create your models here.
class Timer(models.Model):
	start_time = models.PositiveIntegerField(default=0) # change this to DateTimeField
	end_time = models.PositiveIntegerField(default=0) # change this to DateTimeField 
	elapsed_time = models.PositiveIntegerField(default=0) # change this to DateTimeField 
	running_total = models.PositiveIntegerField(default=0) 
	user = models.ForeignKey(User, null=True, blank=True)
	iteration = models.ForeignKey(Iteration, null=True, blank=True)

	def __str__(self):
		return "Timer for %s on iteration %s" % (self.user, self.iteration) 