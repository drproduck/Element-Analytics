"""This module contains all utilities that involves interaction with database"""
import libs.utilities.pathtools as pt
import os
import shutil
from django.contrib.auth.models import User
from apps.upload.models import LogFile


def check_duplicate(current_user, alias):
     """Check if the alias of log file's already existed"""
     duplicate_log_db = current_user.logfile_set.filter(log_name=alias)
     duplicate_log_fs = os.path.exists(pt.get_log_dir_abs(current_user.username, alias))
     if duplicate_log_db or duplicate_log_fs:
          return True
     return False
     

def sync_logdb(user):
     """When logs are accidentally deleted in the database or file system,
         this function will resolve the mismatch between db and file system"""

     # Get log name set in database
     log_list = user.logfile_set.all()
     db_set = set(log.log_name for log in log_list)

     # Get log name in the local file system
     user_dir = pt.get_user_dir_abs(user.username)
     fs_set = set(os.listdir(user_dir))

     # Compute difference between the two
     db_dff = db_set - fs_set
     fs_dff = fs_set - db_set

     # Remove logs in db that is removed in the file system
     user.logfile_set.filter(log_name__in=db_dff).delete()

     # Remove logs in file system that is removed in the database
     for d in fs_set:
          if d in fs_dff:
               abs_dir = os.path.join(user_dir, d)
               shutil.rmtree(abs_dir)


def delete_user(name):
     """Programmatically delete a user and their data in the database"""
     User.objects.filter(username=name).delete();


def delete_log(username, logname):
    """Delete a log of a particular user in the database"""
    
    user = User.objects.filter(pk=username)
    
    # Delete log in the database
    user.logfile_set.filter(log_name=logname).delete()

    # Delete log in file system
    log_dir = pt.get_log_dir_abs(username, logname)
    if not log_dir:
        return
    
    shutil.rmtree(log_dir)
