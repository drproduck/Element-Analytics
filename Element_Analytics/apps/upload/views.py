from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import  login_required

from apps.upload.forms import LogFileForm

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
            form.save()
            # return redirect('home')
            return redirect('/upload')
    else:
        form = LogFileForm()
    return render(request, 'upload/model_form_upload.html', {'form': form})


def filelist(request):
    path = "media/documents"  # insert the path to your directory
    file_list = [f for f in os.listdir(path) if f.startswith('.') == False]
    return render(request, 'upload/filelist.html', {'files': file_list})
