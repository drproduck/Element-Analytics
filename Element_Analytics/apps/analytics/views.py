from django.http import HttpResponse
from django.shortcuts import render
from Element_Analytics.settings import MEDIA_URL
import os
import pandas as pd
# Create your views here.

current_file = None
current_frame = None

def file_home(request, file_name):
    global current_file, current_frame
    path = os.path.join(MEDIA_URL, 'documents/'+file_name)
    if not path.endswith(('.csv', '.log')):
        return HttpResponse("incorrect format")
    current_file = path
    current_frame = pd.read_csv(path)

    return render(request, 'analytics/file_home.html', {'frame':current_frame})
