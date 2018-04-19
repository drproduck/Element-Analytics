"""This module handles log file by parsing input logs
and return a condensed version of the logs with nonessential
information removed. The return data structures can be either
a list of entries or a dataframe supported by Pandas library"""

import os.path
import csv
from libs.parser.tokenizer import GenericTokenizer


def validate_path(path_to_file):
    """check if path is valid"""
    if not os.path.isfile(path_to_file):
        print("File does not exist: ", path_to_file)
        exit()
    if os.stat(path_to_file).st_size == 0:
        print("File is empty: ", path_to_file)
        exit()


def parse_file(path_to_file, user_regex = None):
    """Parse a log file to list of dictionaries"""

    # Set user regex or use default regex
    if user_regex:
        _tkn = GenericTokenizer(user_regex)
    else:
        _tkn = GenericTokenizer()

    validate_path(path_to_file)
    entries = []
    try:
        with open(path_to_file, 'r') as f:
            for l in f:
                # _tkn.parse_line(l)
                entries.append(_tkn.parse_line(l))
    except IOError as e:
        print("Couldn't read file. Error: ", e)
        exit()
    return entries


def to_csv(entries, file_out):
    """Convert logfile to CSV format that can
    be stored on file system and manipulated
    by pandas library"""

    if entries:
        with open(file_out, 'w') as f:
            w = csv.DictWriter(f, entries[0].keys())
            w.writeheader()
            w.writerows(entries)
    else:
        print("error: no data was written")
        exit()
