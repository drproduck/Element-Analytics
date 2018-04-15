from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.upload.forms import LogFileForm
from apps.upload.models import LogFile
from .models import User
from django.http import Http404
import os

import libs.utilities.pathtools as pt


@login_required
def model_form_upload(request):
    """Let user upload file through form"""

    current_user = User.objects.get(pk=request.user.id)

    # Do this if the file is uploaded
    while request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if not form.is_valid():
            break

        # If log name is not specified replace with the name of file
        alias = form.cleaned_data['log_name']
        if not alias:
            alias = pt.filename_no_ext(request.FILES['file'].name)

        # Ignore if log name is duplicate in either database or file system. Need frontend handling!
        # this is wrong. It considers all logs regardless of current user, we only want all logs belong to this user
        # duplicate_log_db = LogFile.objects.filter(log_name=alias)
        duplicate_log_db = current_user.logfile_set.filter(log_name=alias)
        duplicate_log_fs = os.path.exists(pt.get_log_dir_abs(current_user.username, alias))
        if duplicate_log_db or duplicate_log_fs:
            print("This log name already exists")
            break

        # Create new log object in the database
        log = LogFile.objects.create(log_name=alias, file=request.FILES['file'], user=current_user)
        log.save()
        break

    # Do this if the page is initially loaded
    form = LogFileForm()
    return render(request, 'upload/model_form_upload.djt', {'form': form, 'user': current_user})

