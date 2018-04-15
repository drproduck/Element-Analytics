from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import  login_required
from Element_Analytics.settings import DOCUMENT_ROOT
from apps.upload.forms import LogFileForm
from apps.upload.models import LogFile
from .models import User
from django.http import Http404

import os

'''
def home(request):
    documents = Document.objects.all()
    return render(request, 'index/index.html', { 'documents': documents })
'''

'''
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload/simple_upload.html')
'''

@login_required
def model_form_upload(request):
    """Let user upload file through form"""
    current_user = User.objects.get(pk=request.user.id)
    user_name = current_user.username
    user_dir = os.path.join(DOCUMENT_ROOT, user_name)
    if request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if form.is_valid():
            # print(request.user.id)
            #  log dir is used for storing csv file associated with this log file
            log_dir = os.path.join(user_dir, form.cleaned_data['log_name']+'_dir')
            log = LogFile.objects.create(log_name=form.cleaned_data['log_name'],
                                   file=request.FILES['file'], user=current_user,
                                         log_dir=log_dir)
            log.save()
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            return redirect('/upload')
    else:
        form = LogFileForm()
        if not os.path.exists(user_dir):
            raise Http404('Path does not exist. Has the admin migrated new changes to database?')

        file_list = [f for f in os.listdir(user_dir) if not f.endswith('_dir')]
        #for f in file_list:
            #print(f)
        return render(request, 'upload/model_form_upload.djt', {'form': form, 'file_list': file_list})
