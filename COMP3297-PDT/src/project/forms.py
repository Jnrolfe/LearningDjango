from django import forms
from django.contrib.auth.models import User
from .models import Project, Phase, Iteration, DefectData, ReportSLOC

class ProjectForm(forms.ModelForm):
	name = forms.CharField()

	class Meta:
		model = Project
		fields = ['name', 'estimate']

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
		fields = ['project', 'name']

class IterationForm(forms.ModelForm):
	developer = forms.ModelMultipleChoiceField(queryset=User.objects.filter(groups__name='SoftwareDeveloper'), widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Iteration
		fields = ['developer', 'phase', 'name']

class DefectDataForm(forms.ModelForm):
	t1 = 'type 1 Defect'
	t2 = 'type 2 Defect'
	t3 = 'type 3 Defect'
	t4 = 'type 4 Defect'
	DEFECT_CHOICES = (
		(t1, 'type 1 Defect'), 
		(t2, 'type 2 Defect'), 
		(t3, 'type 3 Defect'), 
		(t4, 'type 4 Defect'),
	)

	defect_type = forms.ChoiceField(choices=DEFECT_CHOICES)

	class Meta:
		model = DefectData
		fields = ['defect_iteration', 'current_iteration', 'defect_type', 'defect_description']

class ReportSLOCForm(forms.ModelForm):

	class Meta:
		model = ReportSLOC
		fields = ['total_lines', 'iteration']