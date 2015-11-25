from django import forms

from .models import Timer

class TimerForm(forms.ModelForm):

	class Meta:
		model = Timer
		fields = ['start_time', 'end_time', 'running_total', 'user', 'iteration']
