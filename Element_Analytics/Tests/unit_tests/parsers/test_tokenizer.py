import unittest
# Some hack to add project directoy to PYTHONPATH
from pathlib import Path
import os
import sys
p = Path(os.getcwd()).parent.parent.parent
while p.name != "Element_Analytics":
    p = p.parent
sys.path.append(str(p))
####

from libs.parser.tokenizer import LogTokenizer
import Tests.unit_tests.parsers.golden as g
import libs.parser.logfields as lf

with open("./testlog", 'r') as f:
    input = [line for line in f]


class TestTokenizer(unittest.TestCase):

    lexer = LogTokenizer().build()

    # Test tomcat format
    def test_tomcat(self):
        tomcat = input[0]
        expected = g.golden[0]
        tokens = self.extract_toks(tomcat, self.lexer)
        self.assertEqual(expected[lf.DATE], tokens[0])
        self.assertEqual(expected[lf.NAME], tokens[1])
        self.assertEqual(expected[lf.TYPE], tokens[2])
        self.assertEqual(expected[lf.INFO], tokens[3])
        self.assertEqual(expected[lf.MSSG], tokens[4])

    # Test solr format
    def test_solr(self):
        solr = input[1]
        expected = g.golden[1]
        tokens = self.extract_toks(solr, self.lexer)
        self.assertEqual(expected[lf.DATE], tokens[0])
        self.assertEqual(expected[lf.NAME], tokens[1])
        self.assertEqual(expected[lf.TYPE], tokens[2])
        self.assertEqual(expected[lf.INFO], tokens[3])
        self.assertEqual(expected[lf.MSSG], tokens[4])

    def test_solr1(self):
        solr_commit = input[2]
        expected = g.golden[2]
        tokens = self.extract_toks(solr_commit, self.lexer)
        self.assertEqual(expected[lf.DATE],tokens[0])
        self.assertEqual(expected[lf.NAME],tokens[1])
        self.assertEqual(expected[lf.MSSG],tokens[2])

    # Test nginx format
    def test_nginx(self):
        nginx = input[3]
        expected = g.golden[3]
        tokens = self.extract_toks(nginx, self.lexer)
        self.assertEqual(expected[lf.DATE],tokens[0])
        self.assertEqual(expected[lf.NAME],tokens[1])
        self.assertEqual(expected[lf.INFO],tokens[2])
        self.assertEqual(expected[lf.MSSG],tokens[3])

    def test_nginx1(self):
        nginx = input[4]
        expected = g.golden[4]
        tokens = self.extract_toks(nginx, self.lexer)
        self.assertEqual(expected[lf.DATE], tokens[0])
        self.assertEqual(expected[lf.NAME], tokens[1])
        self.assertEqual(expected[lf.MSSG], tokens[2])

    # Test redis format
    def test_redis(self):
        redis = input[5]
        expected = g.golden[5]
        token = self.extract_toks(redis, self.lexer)
        self.assertEqual(expected[lf.DATE],token[0])
        self.assertEqual(expected[lf.NAME],token[1])
        self.assertEqual(expected[lf.MSSG],token[2])

    # Test iaas format
    def test_iaas(self):
        iaas = input[6]
        expected = g.golden[6]
        token = self.extract_toks(iaas, self.lexer)
        self.assertEqual(expected[lf.DATE],token[0])
        self.assertEqual(expected[lf.NAME],token[1])
        self.assertEqual(expected[lf.TYPE],token[2])
        self.assertEqual(expected[lf.INFO],token[3])
        self.assertEqual(expected[lf.MSSG],token[4])

    def test_iaas1(self):
        iaas = input[7]
        expected = g.golden[7]
        token = self.extract_toks(iaas, self.lexer)
        self.assertEqual(expected[lf.DATE],token[0])
        self.assertEqual(expected[lf.NAME],token[1])
        self.assertEqual(expected[lf.MSSG],token[2])

    def test_iaas2(self):
        iaas = input[8]
        expected = g.golden[8]
        token = self.extract_toks(iaas, self.lexer)
        self.assertEqual(expected[lf.DATE], token[0])
        self.assertEqual(expected[lf.NAME], token[1])
        self.assertEqual(expected[lf.MSSG], token[2])

    # Test cron format
    def test_cron(self):
        cron = input[9]
        expected = g.golden[9]
        token = self.extract_toks(cron, self.lexer)
        self.assertEqual(expected[lf.DATE], token[0])
        self.assertEqual(expected[lf.NAME], token[1])
        self.assertEqual(expected[lf.MSSG], token[2])

    def test_cron1(self):
        cron = input[10]
        expected = g.golden[10]
        token = self.extract_toks(cron, self.lexer)
        self.assertEqual(expected[lf.DATE], token[0])
        self.assertEqual(expected[lf.NAME], token[1])
        self.assertEqual(expected[lf.MSSG], token[2])

    # Test rabbitmq format
    def test_rabbit(self):
        rabbit = input[11]
        expected = g.golden[11]
        token = self.extract_toks(rabbit, self.lexer)
        self.assertEqual(expected[lf.DATE], token[0])
        self.assertEqual(expected[lf.NAME], token[1])

    def test_rabbit1(self):
        rabbit = input[12]
        expected = g.golden[12]
        token = self.extract_toks(rabbit, self.lexer)
        self.assertEqual(expected[lf.DATE], token[0])
        self.assertEqual(expected[lf.NAME], token[1])
        self.assertEqual(expected[lf.MSSG], token[2])


    @staticmethod
    def extract_toks(string, lexer):
        lexer.input(string)
        tokens = [tok.value for tok in lexer]
        return tokens


if __name__ == "__main__":
    unittest.main()