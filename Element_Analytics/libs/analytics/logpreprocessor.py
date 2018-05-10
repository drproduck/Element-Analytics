""" 
This module processes csv's file and return a 
pandas dataframe for analytics module to work with
"""

import libs.utilities.pathtools as pt
import os
import pandas as pd
# import time

from libs.analytics.datetable import DATE_TABLE


class LogNotFoundException(Exception):
    """ Custom exception when
    a log file doesn't exist"""
    pass


def lookup_date(s):
    """ In a large log file dates are mostly repeated so
    we store them in a look up table to improve performance"""
    dates = { date : DATE_TABLE[date[:6]] + date[6:] for date in s.unique() }
    return s.map(dates)


def preprocess(dframe, log_dir, log_name):
    """ Convert date type and save to disk"""
    dframe['date'] = lookup_date(dframe['date'])
    dframe.to_csv(os.path.join(log_dir, log_name + ".csv_preprocessed"))


def read_log(username, log_file):
    """ Read a csv log and turn it in to pandas data frame"""
    log_dir = pt.get_log_dir_abs(username, log_file)
    processed_log = os.path.join(log_dir, log_file + ".csv_preprocessed")
    log = os.path.join(log_dir, log_file + ".csv")

    # If this log is already pre-processed, just return it
    if os.path.isfile(processed_log):
        return pd.read_csv(processed_log,
                           parse_dates=False,
                           encoding='utf-8',
                           error_bad_lines=False,
                           index_col=0)
    elif os.path.isfile(log):
        frame = pd.read_csv(log, parse_dates=False, encoding='utf-8', error_bad_lines=False)
        preprocess(frame, log_dir, log_file)
        return frame
    else:
        raise LogNotFoundException("Log file for this user doesn't exist:" + log)
    return frame

# start_time = time.process_time()
# log = read_log("ly-admin", "syslogClassShare.5")
# elapsed_time = time.process_time() - start_time
# print(elapsed_time)



