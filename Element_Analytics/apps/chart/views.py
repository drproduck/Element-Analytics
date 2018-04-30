from django.shortcuts import render

from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from .fusioncharts import FusionCharts
import json
from .json2chart import json2chart

# it is a default view.
# please go to the samples folder for others view

def chart(request):
    str_keyword, str_date, str_keyword_pie, str_date_pie = json2chart();
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d_keyword = FusionCharts("column2d", "id0" , "700", "350", "chart-1", "json",
        # The data is passed as a string in the `dataSource` as parameter.
    str_keyword)

    column2d_date = FusionCharts("column2d", "id1" , "700", "350", "chart-2", "json",
        # The data is passed as a string in the `dataSource` as parameter.
    str_date)

    pie3d_keyword = FusionCharts("pie3d", "id2" , "700", "350", "chart-3", "json", str_keyword_pie)

    pie3d_date = FusionCharts("pie3d", "id3" , "700", "350", "chart-4", "json", str_date_pie)

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'chart/index.html',
        {'output_keyword' : column2d_keyword.render(), 'output_date' : column2d_date.render(),
        'output_keyword_pie' : pie3d_keyword.render(), 'output_date_pie' : pie3d_date.render()
        })
