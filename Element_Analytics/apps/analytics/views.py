from django.http import HttpResponse
from django.shortcuts import render
from Element_Analytics.settings import MEDIA_URL
import os
import pandas as pd
# Create your views here.

current_file = None

def file_home(request, file_name):
    print(file_name)
    path = os.path.join(MEDIA_URL, 'documents/'+file_name)
    if path.endswith(('.csv', '.log')):
        print('file ok')
    # current_file = pd.read_csv(path)
    return HttpResponse("Hello")
