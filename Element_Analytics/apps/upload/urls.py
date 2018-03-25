from django.conf.urls import url
from apps.upload import views

app_name = 'upload'
urlpatterns = [
    #url('finished/', views.home, name='home'),
    #url(r'^simple/$', views.simple_upload, name='simple_upload'),
    # url('filelist', views.filelist, name='filelist'),
    url('', views.model_form_upload, name='model_form_upload'),
]
