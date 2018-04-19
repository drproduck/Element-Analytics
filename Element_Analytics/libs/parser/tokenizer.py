import re

_DATE = 'date'
_NAME = 'sv_name'
_TYPE = 'type'
_INFO = 'metainfo'
_MSSG = 'message'

default_regex = {
    _DATE : "[A-Za-z]{3}\s[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]+",
    _NAME : "[A-Za-z_]+\[[0-9]+\]",
    _TYPE : "INFO|DEBUG|WARN|ERROR",
    _INFO : "\s+(\.)?[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+",
    _MSSG : "((\s(:|–|-\s-|\*|-)\s)|(:\s[^\[0-9])).+"
}


class GenericTokenizer(object):

    def __init__(self, regex_dict = default_regex):
        self.field = regex_dict
        for key in self.field:
            self.field[key] = re.compile(self.field[key])

    def parse_line(self, line):
        """Tokenize a string"""
        tokens = {}
        for k in self.field:
            regex = self.field[k]
            match = regex.search(line)
            tokens[k] = match.group(0) if match else ""
        return tokens
