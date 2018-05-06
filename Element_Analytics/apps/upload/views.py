from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.upload.forms import LogFileForm
from apps.upload.models import LogFile
from .models import User
import Element_Analytics.settings as settings
import os
import libs.utilities.pathtools as pt
import libs.utilities.dbutils as du
import libs.parser.logparser as parser


@login_required
def model_form_upload(request):
    """Let user upload file through form"""
    current_user = User.objects.get(pk=request.user.id)

    # Sync log database with file system
    # du.sync_logdb(current_user)

    # upload file
    if request.method == 'POST':
        _upload_file(request, current_user)

    # Response
    form = LogFileForm()
    return render(request, 'upload/model_form_upload.djt', {'form': form, 'user': current_user})


def _request_is_valid(request, current_user):

    form = LogFileForm(request.POST, request.FILES)
    if not form.is_valid():
        return False

    uploaded_file = request.FILES['file']
    if not uploaded_file:
        return False

    if current_user.logfile_set.count() >= settings.NUM_LOG_LIMIT:
        print("User attempts to upload more than allowed")
        return False  

    size = pt.get_user_dir_size(current_user.username) + (uploaded_file.size / 2 ** 20)
    if size >= settings.STORAGE_LIMIT:
        print("Not enough storage space")
        return False 
 
    # If log name is not specified replace with the name of uploaded_file
    alias = pt.get_valid_filename(form.cleaned_data['log_name'])
    if not alias:
        alias = pt.get_valid_filename(uploaded_file.name)
    logs = [log.log_name for log in current_user.logfile_set.all()]
    if alias in logs:
        count = 0
        while alias + "_" + str(count) in logs:
            count += 1
        alias += "_" + str(count)
 

    regex = form.cleaned_data['regex']
     
    return (uploaded_file, alias, regex)


def _upload_file(request, current_user):
    """Do this if the file is uploaded"""
    while request.method == 'POST':

        validated = _request_is_valid(request, current_user)
        if not validated:
            break
          
        uploaded_file = validated[0]
        alias = validated[1]
        regex = validated[2]
          
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
        return
    log_dir = pt.get_log_dir_abs(current_user.username, alias)
    out_path = os.path.join(log_dir, alias + ".csv")
    parser.to_csv(data, out_path)
