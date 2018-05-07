import pandas as pd
import libs.analytics.logpreprocessor as lp
import time
import numpy as numpy
import json
import Element_Analytics.settings as settings
import libs.utilities.pathtools as pt
import pprint
import re
# Create your views here.

COMMON_ERROR_KEYS = [
     'exception',
     'warn',
     'error',
     'fail',
     'unauthorized',
     'timeout',
     'refused',
     'NoSuchPageException',
     '404 ',
     '401 ',
     '505 '
]

COMMON_USE_CASES = [
     'DockerServerController',
     'DockerVolumeController',
     'ProvisionController',
     'BlueprintController',
     'ProcessorImpl',
     'MessageHandler',
     'CollectorService',
     'UpdateHandler',
     'SolrCore',
     'LogUpdateProcessor',
     'SolrIndexSearcher'
]


def build_regex(key_list):
    res = "|".join(key_list)
    return re.compile(res)


def error_analytics(dataframe):
    """ Return a JSON object contains insight
    about the errors of this log file"""
    res_dict = {}
    regex = build_regex(COMMON_ERROR_KEYS)
    regex_use = build_regex(COMMON_USE_CASES)
    result = dataframe[dataframe['message'].str.contains(pat=regex) == True]
    result_use = dataframe[dataframe['metainfo'].str.contains(pat=regex_use) == True]
    res_dict['total_entries'] = len(dataframe.index)
    res_dict['num_error'] = len(result.index)
    res_dict['num_use'] = len(result_use.index)
    res_dict['error_rate'] = (res_dict['num_error'] / res_dict['total_entries']) * 100
    res_dict['error_by_keywords'] = count_error_occurences(result)
    res_dict['use_rate'] = (res_dict['num_use'] / res_dict['total_entries']) * 100
    res_dict['use_cases'] = count_use_cases(result_use)
    err_dates = result.groupby(pd.TimeGrouper(key='date', freq='H')).size()
    err_dict = {}
    for name in err_dates.index:
        err_dict[name.ctime()] = err_dates.loc[name]
    res_dict['error_by_dates'] = err_dict
    return json.dumps(res_dict, cls=encoder, indent=4, sort_keys=True)


def user_analytics(user):
    """ Return JSON contains user information"""
    res_dict = {}
    res_dict['username'] = user.username
    res_dict['num_log_limit'] = settings.NUM_LOG_LIMIT
    res_dict['num_log'] = user.logfile_set.count()
    res_dict['storage_limit'] = settings.STORAGE_LIMIT
    res_dict['storage_used'] = pt.get_user_dir_size(user.username)
    return json.dumps(res_dict, indent=4, sort_keys=True)


def count_error_occurences(dataframe):
    error_dict = {}
    for key in COMMON_ERROR_KEYS:
        for row in dataframe[(dataframe.message.str.contains(key))].count():
            error_dict[key] = row
    return error_dict

def count_use_cases(dataframe):
    use_dict = {}
    for key in COMMON_USE_CASES:
        for row in dataframe[(dataframe.metainfo.str.contains(key))].count():
            use_dict[key] = row
    return use_dict

class encoder(json.JSONEncoder):
    """ Customized encoder to encode numpy types"""
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        if isinstance(obj, numpy.float):
            return float(obj)
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return super(encoder, self).default(obj)

# start_time = time.process_time()
# log = lp.read_log("lynguyen", "syslogClassShare.5")
# elapsed_time = time.process_time() - start_time
# error_analytics(log)
# elapsed_time1 = time.process_time() - elapsed_time
# print("read speed: " + str(elapsed_time))
# print("processing speed: " + str(elapsed_time1))
