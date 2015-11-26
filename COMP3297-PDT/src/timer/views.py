from django.shortcuts import render

from .forms import TimerForm
from .models import Timer
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
# Create your views here.

def timer(request):
	title = "set timer"
	form = TimerForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():

		instance = form.save(commit=False)
		instance.user = request.user
		try:
			exist = Timer.objects.get(user=instance.user, iteration=instance.iteration)
			exist.running_total += instance.running_total
			exist.save()
			return HttpResponseRedirect("/thank_you/")
		except Timer.DoesNotExist:
			instance.save()
			return HttpResponseRedirect("/thank_you/")

	return render(request, "start_timer.html", context)