"""This module handles log file by parsing input logs
and return a condensed version of the logs with nonessential
information removed. The return data structures can be either
a list of entries or a dataframe supported by Pandas library"""

from libs.parser.tokenizer import LogTokenizer
import os.path

DATE = 'date'
NAME = 'sv_name'
TYPE = 'type'
INFO = 'metainfo'
MSSG = 'message'

__tokenizer = LogTokenizer().build()

def __validate_path(path_to_file):
    """check if path is valid"""
    if not os.path.isfile(path_to_file):
        print("File does not exist. Exit")
        exit()

def __parse_line(line):
    """parse a single line of log"""
    tokens = {
        DATE : None,
        NAME : None,
        TYPE : None,
        INFO : None,
        MSSG : None
    }
    __tokenizer.input(line)
    for tok in __tokenizer:
        tokens[tok.type] = tok.value
    return tokens


def __append_item(log_dict, token_list):
    """helper: extract items into the dictionary"""
    try:
        log_dict[DATE].append(token_list[DATE])
        log_dict[NAME].append(token_list[NAME])
        log_dict[TYPE].append(token_list[TYPE])
        log_dict[INFO].append(token_list[INFO])
        log_dict[MSSG].append(token_list[MSSG])
    except LookupError as e:
        print(e)
        exit()


def parse_dict_of_lists(path_to_file):
    """parsing the log file and return a
    list of dictionaries representation"""
    __validate_path(path_to_file)
    log_dict = {
        DATE : [],
        NAME : [],
        TYPE : [],
        INFO : [],
        MSSG : []
    }
    try:
        with open(path_to_file, 'r') as f:
            for l in f:
                token_list = __parse_line(l)
                __append_item(log_dict, token_list)
    except IOError as e:
        print("Couldn't read file. Error: ", e)
        exit()

    return log_dict


def parse_list_of_dicts(path_to_file):
    """parse to list of dicts instead of dict of list"""
    __validate_path(path_to_file)
    list = []
    try:
        with open(path_to_file, 'r') as f:
            for l in f:
                list.append( __parse_line(l))
    except IOError as e:
        print("Couldn't read file. Error: ", e)
        exit()
    return list