from django import forms

from .models import Project, Phase, Iteration, DefectData

class ProjectForm(forms.ModelForm):
	name = forms.CharField()

	class Meta:
		model = Project
		fields = ['name', 'is_closed']

class PhaseForm(forms.ModelForm):

	class Meta:
		model = Phase
		fields = ['project', 'name', 'is_closed']

class IterationForm(forms.ModelForm):

	class Meta:
		model = Iteration
		fields = ['developer', 'phase', 'name', 'is_closed']

class DefectDataForm(forms.ModelForm):

	class Meta:
		model = DefectData
		fields = ['iteration', 'total_defects', 'total_lines']