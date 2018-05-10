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


def search(dataframe, keywords, search_field):
    """ Filter out entries that doesn't match keywords"""
    if not keywords:
        keywords = COMMON_ERROR_KEYS
    regex = build_regex(keywords)
    return dataframe[dataframe[search_field].str.contains(pat=regex) == True]


def analytics(dataframe, keywords, search_field):
    """ Helper function that returns result
    according to keywords and search field"""
    res_dict = {}
    result = search(dataframe, keywords, search_field)
    res_dict['total_entries'] = len(dataframe.index)
    res_dict['num_error'] = len(result.index)
    res_dict['error_rate'] = (res_dict['num_error'] / res_dict['total_entries']) * 100
    res_dict['error_by_keywords'] = count_occurences(result, keywords, search_field)
    result['date'] = pd.to_datetime(result['date'], format="%m-%d %H:%M:%S")
    err_dates = result.groupby(pd.Grouper(key='date', freq='H')).size()
    err_dict = {}
    for name in err_dates.index:
        err_dict[name.ctime()] = err_dates.loc[name]
    res_dict['error_by_dates'] = err_dict
    return json.dumps(res_dict, cls=encoder, indent=4, sort_keys=True)


def general_analytics(dataframe, keywords=None, search_field=None):
    """ General case for analytics """
    if not keywords:
        print("WARNING: Keywords list is empty, set to empty string")
        keywords = ''
    if not search_field:
        print("WARNING: search field is empty, set to date")
        search_field = 'date'
    return analytics(dataframe, keywords, search_field)


def error_analytics(dataframe, keywords=None, search_field='message'):
    """ Return a JSON object contains insight
    about the errors of this log file"""
    if not keywords:
        keywords = COMMON_ERROR_KEYS
    return analytics(dataframe, keywords, search_field)


def usercase_analytics(dataframe, keywords=None, search_field='metainfo'):
    """ Return a JSON object contains insight
    about the use cases of this log file"""
    if not keywords:
        keywords = COMMON_USE_CASES
    return analytics(dataframe, keywords, search_field)


def user_analytics(user):
    """ Return JSON contains user information"""
    res_dict = {}
    res_dict['username'] = user.username
    res_dict['num_log_limit'] = settings.NUM_LOG_LIMIT
    res_dict['num_log'] = user.logfile_set.count()
    res_dict['storage_limit'] = settings.STORAGE_LIMIT
    res_dict['storage_used'] = pt.get_user_dir_size(user.username)
    return json.dumps(res_dict, indent=4, sort_keys=True)


def count_occurences(dataframe, keywords, search_field):
    error_dict = {}
    for key in keywords:
        error_dict[key] = len(dataframe[(dataframe[search_field].str.contains(key))])
    return error_dict


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

