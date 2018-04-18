"""
This class represents a generic tokenizer
that can takes a dictionary of fields and
regular expressions to tokenize text instead
of hard coding
"""

import re


class GenericTokenizer(object):
    """This class """
    class Token(object):
        """A token contain a key and value that represent the type of token
        and a substring that match the given pattern"""
        def __init__(self, key, value):
            self.type = key
            self.value = value

    def __init__(self, regex_dict):
        self.field = regex_dict
        self.tokens = []
        self.current = 0
        self.high = 0

    def __iter__(self):
        """This is a iterable class"""
        return self

    def __next__(self):
        """Return the next item """
        if self.current >= self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.tokens[self.current - 1]

    def input(self, line):
        """Tokenize a string"""
        index = 0
        for k in self.field:
            regex = self.field[k]
            match = regex.search(line)
            self.tokens[index].type = k
            self.tokens[index].value = match.group(0) if match else ""
            index += 1
        self.current = 0

    def build(self):
        """Build the tokenizer"""
        for key in self.field:
            self.field[key] = re.compile(self.field[key])
            tok = self.Token(key, "")
            self.tokens.append(tok)
        self.high = len(self.tokens)