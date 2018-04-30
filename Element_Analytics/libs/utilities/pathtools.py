"""Utilities function for paths and file names"""
import os.path as p
import Element_Analytics.settings as settings


def get_ext(path):
     """Get extension of a file"""
     base = p.splitext(p.basename(path))
     if len(base) == 2:
          return base[1]
     return ""


def get_user_dir_rel(username):
     """Get the relative directory of a user"""
     dirs = settings.DOCUMENT_ROOT.split("/")
     doc_root = dirs[len(dirs) - 1]
     return p.join(doc_root, username)


def get_user_dir_abs(username):
     """Get absolute path of user"""
     return p.join(settings.DOCUMENT_ROOT, username)


def get_log_dir_rel(username, logname):
     """Get relative directory of a log"""
     u_dir = get_user_dir_rel(username)
     return p.join(u_dir, logname)


def get_log_dir_abs(username, logname):
     """Get absolute path of log file"""
     u_dir = get_user_dir_abs(username)
     return p.join(u_dir, logname)

