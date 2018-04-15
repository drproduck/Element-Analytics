from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.upload.forms import LogFileForm
from apps.upload.models import LogFile
from .models import User
from django.http import Http404
import os

import libs.utilities.pathtools as pt
import libs.utilities.dbutils as du


@login_required
def model_form_upload(request):
    """Let user upload file through form"""

    current_user = User.objects.get(pk=request.user.id)

    # upload file
    _upload_file(request, current_user)

    # Sync log database with file system
    du.sync_logdb(current_user)

    # Response
    form = LogFileForm()
    return render(request, 'upload/model_form_upload.djt', {'form': form, 'user': current_user})


def _upload_file(request, current_user):
    """Do this if the file is uploaded"""
    while request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if not form.is_valid():
            break

        # If log name is not specified replace with the name of file
        alias = form.cleaned_data['log_name']
        if not alias:
            alias = pt.filename_no_ext(request.FILES['file'].name)

        # Ignore if log name is duplicate in either database or file system. Need frontend handling!
        if du.check_duplicate(current_user, alias):
            print("Invalid name. A log file with that name is existing in the file system")
            break

        # Create new log object in the database
        log = LogFile.objects.create(log_name=alias, file=request.FILES['file'], user=current_user)
        log.save()
        break

