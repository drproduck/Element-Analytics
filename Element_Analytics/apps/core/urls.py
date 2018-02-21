from django.conf.urls import url
from django.urls import path
from apps.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^simple/$', views.simple_upload, name='simple_upload'),
    url(r'^form/$', views.model_form_upload, name='model_form_upload'),
]
