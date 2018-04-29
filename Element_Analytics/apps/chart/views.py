from django.shortcuts import render

from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from .fusioncharts import FusionCharts
import json
from .json2chart import json2chart

# it is a default view.
# please go to the samples folder for others view

def chart(request):
    str_keyword, str_date = json2chart();
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d_keyword = FusionCharts("column2d", "ex1" , "750", "350", "chart-1", "json",
        # The data is passed as a string in the `dataSource` as parameter.
    str_keyword)

    column2d_date = FusionCharts("column2d", "ex2" , "750", "350", "chart-2", "json",
        # The data is passed as a string in the `dataSource` as parameter.
    str_date)

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'chart/index.html', {'output_keyword' : column2d_keyword.render(), 'output_date' : column2d_date.render()})
