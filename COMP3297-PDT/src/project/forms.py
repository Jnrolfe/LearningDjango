from django import forms
from django.contrib.auth.models import User
from .models import Project, Phase, Iteration, DefectData, ReportSLOC

class ProjectForm(forms.ModelForm):
	name = forms.CharField()

	class Meta:
		model = Project
		fields = ['name', 'is_closed']

class PhaseForm(forms.ModelForm):
	INCEPTION = 'Inception'
	ELABORATION = 'Elaboration'
	CONSTRUCTION = 'Construction'
	TRANSITION = 'Transition'
	PHASE_CHOICES = (
		(INCEPTION, 'Inception'), 
		(ELABORATION, 'Elaboration'), 
		(CONSTRUCTION, 'Construction'), 
		(TRANSITION, 'Transition'),
	)
	name = forms.ChoiceField(choices=PHASE_CHOICES)
	
	class Meta:
		model = Phase
		fields = ['project', 'name', 'is_closed']

class IterationForm(forms.ModelForm):
	developer = forms.ModelMultipleChoiceField(queryset=User.objects.filter(groups__name='SoftwareDeveloper'), widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Iteration
		fields = ['developer', 'phase', 'name', 'is_closed']

class DefectDataForm(forms.ModelForm):

	class Meta:
		model = DefectData
		fields = ['defect_iteration', 'current_iteration', 'total_defects', 'defect_description']

class ReportSLOCForm(forms.ModelForm):

	class Meta:
		model = ReportSLOC
		fields = ['total_lines', 'iteration']