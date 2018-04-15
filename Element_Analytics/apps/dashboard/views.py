from django.shortcuts import render
from django.http.response import HttpResponse
from  django.contrib.auth.decorators import login_required
from Element_Analytics.settings import DOCUMENT_ROOT

import os
# Create your views here.

@login_required
def main(request):
    #if request.user.is_authenticated:
        #print("this one is still authenticated")
        #print(request.user.username)
    user = request.user
    username = user.username
    path = os.path.join(DOCUMENT_ROOT, username)
    if not os.path.exists(path):
        os.makedirs(path)
    file_list = [f for f in os.listdir(path) if not f.endswith('_dir')]
    #for f in file_list:
        #print(f)
    return render(request, template_name='dashboard/main.djt', context={'user': user, 'file_list': file_list})
