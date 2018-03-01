from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views
from apps.login.core import views as core_views

urlpatterns = [
    path('', views.login, name='login'),
    url(r'^signup/$', core_views.signup, name='signup'),
]