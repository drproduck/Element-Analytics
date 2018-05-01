from django.conf.urls import url
from apps.upload import views
#from upload.views import delete_file as delete

app_name = 'upload'
urlpatterns = [
    #url('finished/', views.home, name='home'),
    #url(r'^simple/$', views.simple_upload, name='simple_upload'),
    # url('filelist', views.filelist, name='filelist'),
    url('', views.model_form_upload, name='model_form_upload'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_file, name='delete_file')
]
