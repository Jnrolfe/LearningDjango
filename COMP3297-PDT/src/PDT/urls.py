"""PDT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
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
]
