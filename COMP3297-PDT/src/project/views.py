from django.shortcuts import render, render_to_response

from .forms import ProjectForm, PhaseForm, IterationForm, DefectDataForm

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 

# Create your views here.

# everything commented out below is my unsuccessful attempt at putting all the on the project creation page
def project(request):
	title = "create a new project"
	form_a = ProjectForm(request.POST or None)
	# form_b = PhaseForm(request.POST or None)
	# form_c = IterationForm(request.POST or None)
	# form_d = DefectDataForm(request.POST or None)
	context = {
		"title": title,
		"form_a": form_a
		# "form_b": form_b
		# "form_c": form_c
		# "form_d": form_d
	}
	valid_a = form_a.is_valid()
	# valid_b = form_b.is_valid()
	# valid_c = form_c.is_valid()
	# valid_d = form_d.is_valid()
	if valid_a:
		# project form
		instance_a = form_a.save(commit=False)
		manager = form_a.cleaned_data.get("manager")
		instance_a.manager = request.user
		a = instance_a.save()
		# phase form
		# instance_b = form_b.save(commit=False)
		# instance_b.project = a
		# b = instance_b.save()
		# # iteration form
		# instance_c = form_c.save(commit=False)
		# instance_c.phase = b
		# c = instance_c.save()
		# # defect data form
		# instance_d = form_d.save(commit=False)
		# instance_d.phase = c
		# instance_d.save()

	return render(request, "create_project.html", context)

def phase(request):
	title = "create new phase"
	form = PhaseForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		form.save()
	return render(request, "create_phase.html", context)

def iteration(request):
	title = "create new iteration"
	form = IterationForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		form.save()
	return render(request, "create_iteration.html", context)

def defectData(request):
	title = "add defect data"
	form = DefectDataForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		form.save()
	return render(request, "create_defectData.html", context)