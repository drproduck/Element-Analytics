import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.dates import DateFormatter

from Element_Analytics.settings import MEDIA_URL
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from apps.upload.models import User
import seaborn as sb

# Create your views here.

current_file = None
current_file_name = None
current_frame = None
headers = None

def file_home(request, file_name):
    global current_file, current_frame, current_file_name, headers
    current_file_name = file_name
    path = os.path.join(MEDIA_URL, 'documents/'+file_name)
    if not path.endswith(('.csv', '.log')):
        return HttpResponse("incorrect format")
    current_file = path
    current_frame = pd.read_csv(path)
    headers = list(current_frame)

    return render(request, 'analytics/file_home.html', {'name':file_name, 'frame':current_frame,
                                                        'headers':headers})

def variable_plot(request, file_name):
    header = headers[1]
    print(header)
    if request.method == 'POST':
        col_name = request.POST['value']

        # search if temp still has the col_name image
        print(header)
        gr = sb.distplot(current_frame[col_name]).get_figure()
        fig_path = os.path.join(MEDIA_URL, 'temp/' + col_name+'.png')
        gr.savefig(fig_path, format="png")
        plt.close()

    return HttpResponse(open(fig_path, 'rb').read(), content_type="image/png")