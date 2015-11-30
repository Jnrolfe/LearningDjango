from django.contrib import admin

from .models import Project, Phase, Iteration, DefectData, ReportSLOC
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'manager', 'estimate', 'is_closed')
	def save_model(self, request, obj, form, change):
		obj.manager = request.user
		obj.save()

admin.site.register(Project, ProjectAdmin)

class PhaseAdmin(admin.ModelAdmin): 
	list_display = ('project', 'name', 'is_closed')

admin.site.register(Phase, PhaseAdmin)

class IterationAdmin(admin.ModelAdmin):
	list_display = ('phase', 'name', 'is_closed')

admin.site.register(Iteration, IterationAdmin)

class DefectDataAdmin(admin.ModelAdmin):
	list_display = ('defect_iteration', 'defect_type', 'current_iteration')

admin.site.register(DefectData, DefectDataAdmin)

class ReportSLOCAdmin(admin.ModelAdmin):
	list_display = ('total_lines', 'iteration', 'developer')
	def save_model(self, request, obj, form, change):
		obj.developer = request.user
		obj.save()

admin.site.register(ReportSLOC, ReportSLOCAdmin)