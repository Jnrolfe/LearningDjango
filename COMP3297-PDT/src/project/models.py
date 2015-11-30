from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
	manager = models.ForeignKey(User, unique=False, editable=False, null=True, blank=True)
	name = models.CharField("project", max_length=30)
	estimate = models.PositiveIntegerField(default=0, blank=False)
	is_closed = models.BooleanField(default=False)

	def __str__(self):
		return "Project: %s managed by %s" % (self.name, self.manager)

class Phase(models.Model):
	project = models.ForeignKey(Project)
	is_closed = models.BooleanField(default=False)
	name = models.CharField("phase", max_length=30)

	def __str__(self):
		return "Phase: %s of project %s" % (self.name, self.project.name)

class Iteration(models.Model):
	phase = models.ForeignKey(Phase)
	name = models.CharField(max_length=30, blank=False)
	is_closed = models.BooleanField(default=False)
	developer = models.ManyToManyField(User, null=False, blank=True)

	def __str__(self):
		return "Iteration: %s of phase %s of project %s" % (self.name, self.phase.name, self.phase.project.name)

class DefectData(models.Model):
	current_iteration = models.ForeignKey(Iteration, related_name="current_iteration", null=True, blank=True)
	defect_iteration = models.ForeignKey(Iteration, related_name="defect_iteration", null=True, blank=True)
	defect_type = models.CharField(max_length=30, default="type 1 defect")
	developer = models.ForeignKey(User, null=True, blank=True)
	defect_description = models.TextField(blank=True)

	def __str__(self):
		return "Defect Data for iteration: %s" % (self.iteration.name)

class ReportSLOC(models.Model):
	developer = models.ForeignKey(User, null=True, blank=True)
	iteration = models.ForeignKey(Iteration)
	total_lines = models.PositiveIntegerField()

	def __str__(self):
		return "Lines of code completed data for: %s" % (self.developer)

