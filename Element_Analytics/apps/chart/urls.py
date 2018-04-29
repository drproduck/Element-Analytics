"""fusioncharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from samples import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""

from django.conf.urls import url
from django.contrib import admin
from .views import chart

urlpatterns = [

    url('', chart),
]
