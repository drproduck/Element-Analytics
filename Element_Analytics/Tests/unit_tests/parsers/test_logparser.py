import libs.parser.logparser as parser
import Tests.unit_tests.parsers.golden as g
import unittest


with open("./testlog", 'r') as f:
    input = [line for line in f]


class TestParser(unittest.TestCase):

    def test_parseline(self):
        for i in range(0,len(g.golden) - 1):
            self.assertEqual(g.golden[i], parser.parse_line(input[i]))

    def test_parsefile(self):
        self.assertEqual(g.golden, parser.parse_file("./testlog"))

    def test_parsefile_threading(self):
        res = parser.parse_file_parallel("./testlog")
        for item in res:
            self.assertIn(item, g.golden)

if __name__ == "__main__":
    unittest.main()