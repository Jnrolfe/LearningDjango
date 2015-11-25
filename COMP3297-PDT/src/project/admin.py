from django.contrib import admin

from .models import Project, Phase, Iteration, DefectData
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'manager', 'is_closed')
	def save_model(self, request, obj, form, change):
		obj.manager = request.user
		obj.save()

admin.site.register(Project, ProjectAdmin)

class PhaseAdmin(admin.ModelAdmin):
	list_display = ('project', 'name', 'is_closed')

admin.site.register(Phase, PhaseAdmin)

class IterationAdmin(admin.ModelAdmin):
	list_display = ('developer', 'phase', 'name', 'is_closed')

admin.site.register(Iteration, IterationAdmin)

class DefectDataAdmin(admin.ModelAdmin):
	list_display = ('iteration', 'total_defects', 'total_lines')

admin.site.register(DefectData, DefectDataAdmin)