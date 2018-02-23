from django.http import HttpResponse
from django.shortcuts import render
from Element_Analytics.settings import MEDIA_URL
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
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

    return render(request, 'analytics/file_home.html', {'frame':current_frame, 'file_name':file_name,
                                                        'headers':headers})

def variableplot(request):
    header = headers[1]
    if request.method == 'POST':
        header = request.POST['value']
        print(header)
    col = current_frame[header]
    # canvas = FigureCanvas(plt.hist(col))

    fig=Figure()
    ax=fig.add_subplot(111)
    ax.hist(col)
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response