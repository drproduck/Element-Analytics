""" Analytics view module """
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from Element_Analytics.settings import BASE_DIR


STATIC_DIR = os.path.join(BASE_DIR, 'apps/analytics/static/analytics/')


@login_required
def main_view(request, log_name):
    """ Analytics main view """
    return render(request, "analytics/mainpage.djt", {"log_name" : log_name})
    
