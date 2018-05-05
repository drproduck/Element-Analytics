""" Analytics view module """
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

import libs.utilities.pathtools  as pt
from Element_Analytics.settings import BASE_DIR


STATIC_DIR = os.path.join(BASE_DIR, 'apps/analytics/static/analytics/')


def get_user_log_dir(user,  log):
    """root -> user dir -> log dir -> bunch of .csv and a single .raw"""
    return pt.get_log_dir_abs(user, log ) + ".csv"


@login_required
def main_view(request, log_name):
    """ Analytics main view """
    user = request.user
    file_path = os.path.join(pt.get_log_dir_abs(user.username, log_name), log_name + ".csv")
    logfile = user.logfile_set.get(log_name=log_name)
    if not logfile.regex:
        return render(request, "analytics/mainpage.djt", {"log_name" : log_name})
    with open(file_path, 'r') as fp:
        response = HttpResponse(fp.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + log_name + ".csv"
        return response
