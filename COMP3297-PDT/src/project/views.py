# django imports
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
# my imports
from .forms import ProjectForm, PhaseForm, IterationForm, DefectDataForm, ReportSLOCForm
from .models import Project, Phase, Iteration, DefectData, ReportSLOC
from timer.models import Timer as timer_model
from datetime import datetime, timedelta

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
		try:
			exist = ReportSLOC.objects.get(developer=instance.developer, iteration=instance.iteration)
			exist.total_lines += instance.total_lines
			exist.save()
			return HttpResponseRedirect("/thank_you/")
		except ReportSLOC.DoesNotExist:
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
		proj_lines = 0
		for i in phases:
			phaseList.append(i)
			iterations = Iteration.objects.filter(phase=i)
			if iterations != None:
				for ite in iterations:
					reports = ReportSLOC.objects.filter(iteration=ite)
					if reports != None:
						for r in reports:
							proj_lines += r.total_lines
		context = {
			"projSLOC": proj_lines,
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
		phaseSLOC = 0
		for i in iterations:
			iterationList.append(i)
			reports = ReportSLOC.objects.filter(iteration=i)
			if reports != None:
				for r in reports:
					phaseSLOC += r.total_lines
		context = {
			"phaseSLOC": phaseSLOC,
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
		dev_line_list = []
		
		# iteration total sloc
		for i in slocs:
			slocs_total_lines += i.total_lines
			sloc_devs_set.add(i.developer)
			temp = ReportSLOC.objects.filter(iteration=iteration, developer=i.developer)
			if temp != None:
				for a in temp:
					dev_line_list.append(a)

		context = {
			"sloc_devs": sloc_devs_set,
			"dev_line_list": dev_line_list,
			"sloc_total": slocs_total_lines,
			"iteration": iteration
		}
		
	except ReportSLOC.DoesNotExist:
		context = {
			"iteration": iteration
		}
	# try:
	# 	times = timer_model.objects.filter(iteration=iteration)
	# 	times_total = 0

	# 	for i in times:
	# 		times_total += i.running_total

	# 	context = {
	# 		"times_total": times_total
	# 	}
	# except timer_model.DoesNotExist:
	# 	context = {
	# 		"iteration": iteration
	# 	}

	return render(request, "show_iteration_detail.html", context)

def viewMyDefects(request):
	p = request.POST
	User = request.user
	try:
		defects = DefectData.objects.filter(developer=User)
		context = {
			"defects": defects
		}
	except DefectData.DoesNotExist:
		msg = "No Defect data found for: "+str(User)
		context = {
			"error_msg": msg
		}

	return render(request, "view_my_defects.html", context)

def viewMySLOC(request):
	p = request.POST
	User = request.user
	try:
		mySLOCs = ReportSLOC.objects.filter(developer=User)
		context = {
			"mySLOCs" : mySLOCs
		}
	except ReportSLOC.DoesNotExist:
		msg = "No SLOC data found for: "+str(User)
		context = {
			"error_msg": msg
		}

	return render(request, "view_my_SLOC.html", context)

def viewMyTime(request):
	p = request.POST
	User = request.user
	try:
		myTimes = timer_model.objects.filter(user=User)
		context = {
			"myTimes" : myTimes
		}
	except timer_model.DoesNotExist:
		msg = "No Time data found for: "+str(User)
		context = {
			"error_msg": msg
		}

	return render(request, "view_my_times.html", context)

def manageProjects(request):
	p = request.POST
	User = request.user
	try:
		projects = Project.objects.filter(manager=User)
		context = {
			"projects": projects
		}
		
	except Project.DoesNotExist:
		msg = "No project data found for: "+str(User)

	return render(request, "manage_projects.html", context)

def closeProjects(request):
	p = request.POST
	p_id = p['close']
	close_proj = Project.objects.get(pk=p_id)
	close_proj.is_closed = True
	close_proj.save()
	return HttpResponseRedirect("/thank_you/")

# add open and close projects, phases, iterations
# filter all project, phase, and iterations by is_closed of self, phase, project
