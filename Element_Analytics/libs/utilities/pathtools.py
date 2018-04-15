"""Utilities function for paths and file names"""
import os.path as p
import Element_Analytics.settings as settings


# Get name o file without extension
def filename_no_ext(path):
    base = p.basename(path)
    name = p.splitext(base)[0]
    return name


# Get extension of a file
def get_ext(path):
    base = p.splitext(p.basename(path))
    if len(base) == 2:
        return base[1]
    return ""


# Get the relative directory of a user
def get_user_dir_rel(user):
    dirs = settings.DOCUMENT_ROOT.split("/")
    doc_root = dirs[len(dirs) - 1]
    return p.join(doc_root, user)


# Get relative directory of a log
def get_log_dir_rel(user, log):
    u_dir = get_user_dir_rel(user)
    return p.join(u_dir, log)


# Get absolute path of user
def get_user_dir_abs(user):
    return p.join(settings.DOCUMENT_ROOT, user)


# Get absolute path of log file
def get_log_dir_abs(user, log):
    u_dir = get_user_dir_abs(user)
    return p.join(u_dir, log)