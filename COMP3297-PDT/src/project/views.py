# django imports
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
# my imports
from .forms import ProjectForm, PhaseForm, IterationForm, DefectDataForm, ReportSLOCForm
from .models import Project, Phase, Iteration, DefectData, ReportSLOC

# Create your views here.

###########################################################
######################### Forms ###########################
###########################################################

# create project form
def project(request):
	title = "create a new project"
	form = ProjectForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	} 
	if form.is_valid():
		instance = form.save(commit=False)
		instance.manager = request.user
		instance.save()
		return HttpResponseRedirect("/thank_you/")

	return render(request, "create_project.html", context)

# create phase form
def phase(request):
	title = "create new phase"
	form = PhaseForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/thank_you/")
	return render(request, "create_phase.html", context)

# create iteration form
def iteration(request):
	title = "create new iteration"
	form = IterationForm(request.POST or None)
	# form.fields['developer'].queryset = User.objects.filter(groups__name='SoftwareDeveloper')
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/thank_you/")
	return render(request, "create_iteration.html", context)

# add new Defect Data
def defectData(request):
	title = "add defect data"
	form = DefectDataForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/thank_you/")
	return render(request, "create_defectData.html", context)

def reportSLOC(request):
	title = "add source lines of code"
	form = ReportSLOCForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.developer = request.user
		instance.save()
		return HttpResponseRedirect("/thank_you/")


	return render(request, "report_SLOC.html", context)

def thankYou(request):
	return render(request, "thank_you.html", {})

###########################################################
######################### Queries #########################
###########################################################

def viewProjects(request):
	User = request.user
	# get projects the current user is manager of
	projects = Project.objects.filter(manager=User)
	
	# get phases associated with projects
	phaseList = []
	for i in projects:
		p = Phase.objects.get(project=i)
		phaseList.append(p)

	# get iterations associated with phases
	iterationList = []
	for i in phaseList:
		iterationList.append(Iteration.objects.get(phase=i))

	context = {
		"projects": projects,
		"phases": phaseList,
		"iterations": iterationList
	}

	return render(request, "view_projects.html", context)

