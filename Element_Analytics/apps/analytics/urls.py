from django.conf.urls import url
from django.urls import path, re_path

from apps.analytics import views

app_name = 'analytics'
urlpatterns = [
    re_path(r'(?P<file_name>\w+)/', views.file_home, name='file_home'),
]