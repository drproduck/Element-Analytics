from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.shortcuts import loader
from django.views import View
# Create your views here.


class MainView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/dashboard")
        page = loader.get_template('index/index.djt')
        return HttpResponse(page.render())

