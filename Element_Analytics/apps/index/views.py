from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import loader
from django.views import View
# Create your views here.


class MainView(View):
    def get(self, request, *args, **kwargs):
        page = loader.get_template('index/index.html')
        return HttpResponse(page.render())

