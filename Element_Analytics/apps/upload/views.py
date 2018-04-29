from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.upload.forms import LogFileForm
from apps.upload.models import LogFile
from .models import User
import os
import libs.utilities.pathtools as pt
import libs.utilities.dbutils as du
import libs.parser.logparser as parser

@login_required
def model_form_upload(request):
    """Let user upload file through form"""
    current_user = User.objects.get(pk=request.user.id)

    # Sync log database with file system
    du.sync_logdb(current_user)

    # upload file
    if request.method == 'POST':
        _upload_file(request, current_user)

    # Response
    form = LogFileForm()
    return render(request, 'upload/model_form_upload.djt', {'form': form, 'user': current_user})


def _upload_file(request, current_user):
    """Do this if the file is uploaded"""
    while request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if not form.is_valid():
            break

        uploaded_file = request.FILES['file']
        if not uploaded_file:
            break

        # If log name is not specified replace with the name of uploaded_file
        alias = form.cleaned_data['log_name']
        if not alias:
            alias = uploaded_file.name

        # If regex is not specified replace it with empty string
        regex = form.cleaned_data['regex']

        # Ignore if log name is duplicate in either database or uploaded_file system. Need frontend handling!
        if du.check_duplicate(current_user, alias):
            print("Invalid name. A log uploaded_file with that name is existing in the uploaded_file system")
            break

        # Create new log object in the database
        log = LogFile.objects.create(log_name=alias, file=uploaded_file, user=current_user, regex=regex)
        log.save()

        # Parse the uploaded log file
        _parse_file(current_user, uploaded_file, alias, regex)
        break


def _parse_file(current_user, log_file, alias, regex):
    """Parse log file"""
    print("Parsing file..")
    with log_file.open("r") as file:
        data = parser.parse_file(file, regex)
    print("Writing file...")
    if not data:
        print("File is empty")
        return;
    log_dir = pt.get_log_dir_abs(current_user.username, alias)
    out_path = os.path.join(log_dir, alias + ".csv")
    parser.to_csv(data, out_path)
