from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from .models import Timer

class TimerForm(forms.ModelForm):

	class Meta:
		model = Timer
		fields = ['iteration', 'running_total']
