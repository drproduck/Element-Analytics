from django.conf.urls import url
from django.urls import path, re_path

from apps.analytics import views

app_name = 'analytics'
urlpatterns = [
    path('<file_name>/', views.file_home, name='file_home'),
    path('<file_name>/variable_plot.png',views.variable_plot, name='variable_plot')
]