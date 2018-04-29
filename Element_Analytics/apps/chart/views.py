from django.shortcuts import render

from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from .fusioncharts import FusionCharts
import json

# it is a default view.
# please go to the samples folder for others view

def chart(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1" , "1050", "700", "chart-1", "json",
        # The data is passed as a string in the `dataSource` as parameter.
    """{
        "chart": {
            "caption": "Error analytics",
            "subCaption": "",
            "xAxisName": "keyword",
            "yAxisName": "count",
            "numberPrefix": "",
            "theme": "fint"
        },
        "data": [
            {"label": "exception", "value": "42"},
            {"label": "warn", "value": "81"},
            {"label": "error", "value": "72"},
            {"label": "fail", "value": "55"},
            {"label": "unauthorized", "value": "91"},
            {"label": "timeout", "value": "51"},
            {"label": "refused", "value": "68"},
            {"label": "NoSuchPageException", "value": "62"},
            {"label": "404", "value": "61"},
            {"label": "401", "value": "49"},
            {"label": "500", "value": "90"}
        ]
    }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output' : column2d.render()})
