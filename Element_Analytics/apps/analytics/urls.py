from django.conf.urls import url
from django.urls import path, re_path
import tabulate
from apps.analytics import views

app_name = 'analytics'

urlpatterns = [
     path('', views.MainView)
]