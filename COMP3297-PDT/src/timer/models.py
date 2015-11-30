from django.db import models
from django.contrib.auth.models import User
from project.models import Iteration

# Create your models here.
class Timer(models.Model):
	start_time = models.DateTimeField(null=True, blank=True)
	end_time = models.DateTimeField(null=True, blank=True)
#	elapsed_time = models.DecimalField(max_digits=7, decimal_places=1, default=0.0) # we only use running total
	running_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) # running total in hours
	user = models.ForeignKey(User, null=True, blank=True)
	iteration = models.ForeignKey(Iteration, null=True, blank=True)
	is_running= models.NullBooleanField()

	def __str__(self):
		return "Timer for %s on iteration %s" % (self.user, self.iteration) 