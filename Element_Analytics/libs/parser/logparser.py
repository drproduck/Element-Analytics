"""This module handles log file by parsing input logs
and return a condensed version of the logs with nonessential
information removed. The return data structures can be either
a list of entries or a dataframe supported by Pandas library"""

from libs.parser.tokenizer import LogTokenizer
import os.path
import libs.parser.logfields as field


tokenizer = LogTokenizer().build()


def validate_path(path_to_file):
    """check if path is valid"""
    if not os.path.isfile(path_to_file):
        print("File does not exist. Exit")
        exit()


def parse_line(line):
    """parse a single line of log"""
    tokens = {
        field.DATE : None,
        field.NAME : None,
        field.TYPE : None,
        field.INFO : None,
        field.MSSG : None
    }
    tokenizer.input(line)
    for tok in tokenizer:
        tokens[tok.type] = tok.value
    return tokens


def parse_file(path_to_file):
    """parse a log file into a list of log entries in dictionaries"""
    validate_path(path_to_file)
    list = []
    try:
        with open(path_to_file, 'r') as f:
            for l in f:
                list.append(parse_line(l))
    except IOError as e:
        print("Couldn't read file. Error: ", e)
        exit()
    return list