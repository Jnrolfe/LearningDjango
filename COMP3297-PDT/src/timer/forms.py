from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from .models import Timer

class TimerForm(forms.ModelForm):

	class Meta:
		model = Timer
		fields = ['iteration', 'start_time']

class StopTimerForm(forms.ModelForm):
	class Meta:
		model = Timer
		fields = ['iteration', 'start_time', 'end_time']