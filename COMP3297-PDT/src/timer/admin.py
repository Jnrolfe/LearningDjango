from django.contrib import admin

from .models import Timer
# Register your models here.

class TimerAdmin(admin.ModelAdmin):
	list_display = ('start_time', 'end_time', 'running_total', 'user', 'iteration')

admin.site.register(Timer, TimerAdmin)