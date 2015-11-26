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
	context = {
		"projects": projects
	}

	return render(request, "view_projects.html", context)

def showProjectDetail(request):
	p = request.POST
	p_id = p['pro']
	proj = Project.objects.get(pk=p_id)
	try:
		phases = Phase.objects.filter(project=proj)
		phaseList = []
		for i in phases:
			phaseList.append(i)
		context = {
			"project": proj,
			"phases": phaseList
		}
	except Phase.DoesNotExist:
		context = {
			"project": proj
		}
	return render(request, "show_project_detail.html", context)

def showPhaseDetail(request):
	p = request.POST
	p_id = p['pha']
	phase = Phase.objects.get(pk=p_id)
	try:
		iterations = Iteration.objects.filter(phase=phase)
		iterationList = []
		for i in iterations:
			iterationList.append(i)
		context = {
			"phase": phase,
			"iterations": iterationList
		}
	except Iteration.DoesNotExist:
		context = {
			"phase": phase
		}
	return render(request, "show_phase_detail.html", context)

def showIterationDetail(request):
	p = request.POST
	p_id = p['ite']
	iteration = Iteration.objects.get(pk=p_id)
	try:
		slocs = ReportSLOC.objects.filter(iteration=iteration)
		slocs_total_lines = 0
		sloc_devs_set = set()
		
		# iteration total sloc
		for i in slocs:
			slocs_total_lines += i.total_lines
			sloc_devs_set.add(i.developer)

		# developer specific total
		dev_line_list = []
		for dev in sloc_devs_set:
			devs_reports = ReportSLOC.objects.filter(developer=dev)
			devs_line_total = 0
			for report in devs_reports:
				devs_line_total += report.total_lines
			dev_line_list.append(devs_line_total)

		context = {
			"sloc_devs": sloc_devs_set,
			"dev_line_list": dev_line_list,
			"sloc_total": slocs_total_lines,
			"iteration": iteration
		}
	except Iteration.DoesNotExist:
		context = {
			"iteration": iteration
		}
	return render(request, "show_iteration_detail.html", context)

