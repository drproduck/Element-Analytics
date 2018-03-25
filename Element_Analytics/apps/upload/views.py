from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import  login_required
from Element_Analytics.settings import MEDIA_URL
from apps.upload.forms import LogFileForm
from apps.upload.models import LogFile
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.user.id)
            log = LogFile.objects.create(file_name=request.POST['file_name'],
                                   file=request.FILES['file'], user=User.objects.get(pk=request.user.id))
            log.save()
            return redirect('/upload')
    else:
        form = LogFileForm()
        user = request.user
        username = user.username
        path = MEDIA_URL+'document/'+username+'/'
        print(path)
        if not os.path.exists(path):
            os.makedirs(path)
        file_list = [f for f in os.listdir(path)]
        for f in file_list:
            print(f)
        return render(request, 'upload/model_form_upload.html', {'form': form, 'file_list': file_list})


