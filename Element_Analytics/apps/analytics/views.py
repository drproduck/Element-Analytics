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
import ray.dataframe as pdr

# Create your views here.

current_file = None
current_file_name = None
current_frame = None
headers = None
temp_dir = None
path = None
MAX_TEMP_FIG = 5

def file_home(request, file_name):
    global current_file, current_frame, current_file_name, headers, temp_dir, path
    current_file_name = file_name
    path = os.path.join(MEDIA_URL, 'documents/'+file_name)
    temp_dir = os.path.join(MEDIA_URL, 'temp/'+file_name+'/')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
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

        fig_path = os.path.join(temp_dir, col_name + '.png')
        if not os.path.exists(fig_path):
            gr = sb.distplot(current_frame[col_name]).get_figure()
            gr.savefig(fig_path, format="png")
            plt.close()

        # if number of temp files > MAX_TEMP_FIG, remove earliest
        temp_files = [os.path.join(temp_dir, f) for f in os.listdir(temp_dir)]
        fig_files = [f for f in temp_files if f.endswith('.png') == True]
        print(fig_files)
        if len(fig_files) > MAX_TEMP_FIG:
            _, f = min([(os.path.getctime(f), f) for f in fig_files])
            os.remove(f)
        print(header)

    return HttpResponse(open(fig_path, 'rb').read(), content_type="image/png")
