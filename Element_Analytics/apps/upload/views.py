from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from apps.upload.models import Document
from apps.upload.forms import DocumentForm

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

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('home')
            return redirect('/upload')
    else:
        form = DocumentForm()
    return render(request, 'upload/model_form_upload.html', {'form': form})

def filelist(request):
    path = "media/documents"  # insert the path to your directory
    file_list = [f for f in os.listdir(path) if f.startswith('.') == False]
    return render(request, 'upload/filelist.html', {'files': file_list})
