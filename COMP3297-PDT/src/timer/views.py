from django.shortcuts import render
from .forms import TimerForm, StopTimerForm
from .models import Timer
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
from datetime import datetime, timedelta
from decimal import *
from django.http import Http404
# Create your views here.

def timer(request):

#get all timer record by user


	working = 0
	records = Timer.objects.filter(user=request.user)
	for r in records:
		if r.is_running == True:
			working = r
	if working!=0:

########found running timer
		title="Stop Timer"
		form = StopTimerForm(request.POST or None, initial={'iteration' : working.iteration, 'start_time': working.start_time, 'end_time': datetime.now})
		form.fields['iteration'].widget.attrs['disabled'] = True

	else:
########no running timer found
		form = TimerForm(request.POST or None, initial={'start_time': datetime.now})
		title="Start Timer"


	context = {
		"title": title,
		"form": form
	}

	if form.is_valid() and working==0:

		instance = form.save(commit=False)
		instance.user = request.user
		try:
			exist = Timer.objects.get(user=request.user, iteration=instance.iteration)
			exist.start_time = instance.start_time
			exist.end_time=None
			exist.is_running=1
			exist.save()
			return HttpResponseRedirect("/thank_you/")
		except Timer.DoesNotExist:
			instance.is_running=1
			instance.save()
			return HttpResponseRedirect("/thank_you/")

	if form.is_valid() and working!=0:

		instance = form.save(commit=False)
		instance.user = request.user
		timeadd=(instance.end_time-instance.start_time).days*24+(instance.end_time-instance.start_time).seconds/3600
		try:
			exist = Timer.objects.get(user=working.user, iteration=working.iteration)
			exist.running_total+=Decimal("%.2f"% timeadd)
			exist.end_time=instance.end_time
			exist.is_running=0
			exist.save()
			return HttpResponseRedirect("/thank_you/")
		except Timer.DoesNotExist:
			raise Http404
			return HttpResponseRedirect("/thank_you/")

	return render(request, "start_timer.html", context)