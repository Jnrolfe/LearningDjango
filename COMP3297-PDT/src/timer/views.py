from django.shortcuts import render

from .forms import TimerForm

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
# Create your views here.

def timer(request):
	title = "start timer"
	form = TimerForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	return render(request, "start_timer.html", context)