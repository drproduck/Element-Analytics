import re

default_regex = "date -> [A-Za-z]{3}\s[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]+\n\
                sv_name -> [A-Za-z_]+\[[0-9]+\]\n\
                type -> INFO|DEBUG|WARN|ERROR\n\
                metainfo -> \s+(\.)?[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+\n\
                message -> ((\s(:|–|-\s-|\*|-)\s)|(:\s[^\[0-9])).+"


class GenericTokenizer(object):

    def __init__(self, regex=default_regex):
        self.field = process_regex(regex)
        if not self.field:
            self.field = process_regex(default_regex)
        for key in self.field:
            # self.field[key] = re.compile(bytes(self.field[key], "utf-8"))
            self.field[key] = re.compile(self.field[key])

    def parse_line(self, line):
        """Tokenize a string"""
        tokens = {}
        for k in self.field:
            regex = self.field[k]
            match = regex.search(line)
            tokens[k] = match.group(0) if match else ""
        return tokens


def process_regex(regex):
    """ This function parse a regex string
    into a dictionary of fields and regexes
    Format: <field1> -> <regex1>
            <field2 -> <regex2> etc."""
    res_dict = {}
    lines = regex.split("\n")
    for l in lines:
        tok = l.split("->")
        if len(tok) != 2:
            continue
        field = tok[0].strip(" \t\n\r")
        rg = tok[1].strip(" \t\n\r")
        res_dict[field] = rg
    return res_dict

