"""PDT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'index.views.index', name='index'),
    url(r'^$', 'authen.views.auth_login', name = "auth_login"),
    url(r'^logout/', 'authen.views.auth_logout', name = "auth_logout"),
    url(r'^create_project/', 'project.views.project', name = "create_project"),
    url(r'^create_phase/', 'project.views.phase', name = "create_phase"),
    url(r'^create_iteration/', 'project.views.iteration', name = "create_iteration"),
    url(r'^create_defectData/', 'project.views.defectData', name = "create_defectData"),
    url(r'^start_timer/', 'timer.views.timer', name = "start_timer"),
    url(r'^view_projects/', 'project.views.viewProjects', name = "view_projects"),
    url(r'^report_sloc/', 'project.views.reportSLOC', name = "report_sloc"),
    url(r'^thank_you/', 'project.views.thankYou', name = "thank_you"),
    url(r'^show_project_detail/', 'project.views.showProjectDetail', name = "show_project_detail"),
    url(r'^show_phase_detail/', 'project.views.showPhaseDetail', name = "show_phase_detail"),
    url(r'^show_iteration_detail/', 'project.views.showIterationDetail', name = "show_iteration_detail"),
    url(r'^view_my_defects/', 'project.views.viewMyDefects', name = "view_my_defects"),
    url(r'^view_my_times/', 'project.views.viewMyTime', name = "view_my_times"),
    url(r'^view_my_SLOC/', 'project.views.viewMySLOC', name = "view_my_SLOC"),
    url(r'^manage_projects/', 'project.views.manageProjects', name = "manage_projects"),
    url(r'^close_projects/', 'project.views.closeProjects', name = "close_projects"),
]

