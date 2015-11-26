# django imports
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
# my imports
from .forms import ProjectForm, PhaseForm, IterationForm, DefectDataForm
from .models import Project, Phase, Iteration, DefectData

# Create your views here.

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
		manager = form.cleaned_data.get("manager")
		instance.manager = request.user
		instance.save()

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
	return render(request, "create_defectData.html", context)

def viewProjects(request):
	User = request.user
	# get projects the current user is manager of
	p = Project.objects.filter(manager=User)
	projects = []
	for i in p:
		projects.append(i)

	# get phases associated with projects
	phaseList = []
	for i in projects:
		phaseList.append(Phase.objects.filter(project=i))

	# get iterations associated with phases
	iterationList = []
	for i in phaseList:
		iterationList.append(Iteration.objects.filter(phase=i))

	context = {
		"projects": projects,
		"phases": phaseList,
		"iterations": iterationList
	}

	return render(request, "view_projects.html", context)