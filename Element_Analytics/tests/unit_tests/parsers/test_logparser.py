# Some hack to add project directoy to PYTHONPATH
from pathlib import Path
import os
import sys
p = Path(os.getcwd()).parent.parent.parent
while p.name != "Element_Analytics":
    p = p.parent
sys.path.append(str(p))
####

import unittest
from libs.parser.tokenizer import GenericTokenizer
import libs.parser.logparser as parser
import tests.unit_tests.parsers.golden as g


with open("./testlog", 'r') as f:
    input = [line for line in f]


class TestParser(unittest.TestCase):

    def test_parseline(self):
        lexer = GenericTokenizer()
        for i in range(0,len(g.golden) - 1):
            self.assertEqual(g.golden[i], lexer.parse_line(input[i]))

    def test_parsefile(self):
        self.assertEqual(g.golden, parser.parse_file("./testlog"))


if __name__ == "__main__":
    unittest.main()