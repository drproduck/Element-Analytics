"""This module handles log file by parsing input logs
and return a condensed version of the logs with nonessential
information removed. The return data structures can be either
a list of entries or a dataframe supported by Pandas library"""

import os.path
import csv
from libs.parser.tokenizer import GenericTokenizer


def parse_file(file, user_regex = None):
    """Parse a log file to list of dictionaries"""

    # Set user regex or use default regex
    if user_regex:
        _tkn = GenericTokenizer(user_regex)
    else:
        _tkn = GenericTokenizer()

    entries = []
    try:
        for l in file:
            line = l.decode("utf-8")
            entries.append(_tkn.parse_line(line))
    except IOError as e:
        print("Couldn't read file. Error: ", e)
        file.close()
        exit()
    return entries


def to_csv(entries, file_out):
    """Convert logfile to CSV format that can
    be stored on file system and manipulated
    by pandas library"""

    if not  entries:
        print("Error: Data object is empty")
        return

    if entries:
        with open(file_out, 'w') as f:
            w = csv.DictWriter(f, entries[0].keys())
            w.writeheader()
            w.writerows(entries)
    else:
        print("error: no data was written")
        exit()
