from django.contrib.auth.models import User

from django.db import models

import os.path
import libs.utilities.pathtools as pt


# Return the path of a newly uploaded log file
def get_store_path(file_instance, filename):
    un = file_instance.get_username()
    ln = file_instance.log_name
    log_dir = pt.get_log_dir_rel(un, ln)  # Get relative path
    abs_path = pt.get_log_dir_abs(un, ln)  # Get absolute path
    if not os.path.exists(abs_path):  # If path to log doesn't exist, create one
        os.mkdir(abs_path)
    return os.path.join(log_dir, ln)


# Log file model
class LogFile(models.Model):

    def get_username(self):
        return self.user.username

    def get_filepath(self):
        return self.file.path

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=get_store_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    regex = models.TextField(null=True, blank=True)

