from django.http import HttpResponse
from django.shortcuts import render, redirect
from Element_Analytics.settings import MEDIA_URL
from Element_Analytics.settings import DOCUMENT_ROOT, BASE_DIR
from ..upload.models import LogFile
import libs.utilities.pathtools  as pt

import os
import pandas as pd

from django.contrib.auth.decorators import login_required

STATIC_DIR = os.path.join(BASE_DIR, 'apps/analytics/static/analytics/')


def get_user_log_dir(user,  log):
     """root -> user dir -> log dir -> bunch of .csv and a single .raw"""
     return pt.get_log_dir_abs(user, log ) + ".csv"


@login_required
def MainView(request):
     if request.POST:
          return render()

