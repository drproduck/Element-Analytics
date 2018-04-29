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
import cProfile
import time
import libs.parser.logparser as parser


class TestPerformance(unittest.TestCase):

    # @unittest.skip
    def test_parser(self):
        filename = "/home/lynux/workspace/Element-Analytics/logs/og/syslogClassShare.5"
        outfile = "./out.csv"

        print("Processing...\n")
        start = time.time()
        with open(filename, "rb") as file:
            res = parser.parse_file(file)
        elapsed_time = time.time() - start
        print("Process time: ", elapsed_time, "\n")
        self.assertLess(elapsed_time, 60)

        print("Writing CSV...\n")
        start = time.time()
        parser.to_csv(res, outfile)
        elapsed_time = time.time() - start
        print("Write time: ", elapsed_time, "\n")
        self.assertLess(elapsed_time, 30)

        print("# of log entries processed: ", len(res))

    @unittest.skip
    def test_parser_profiling(self):
        filename = input("Filename: ")
        outfile = input("Output file: ")
        pr = cProfile.Profile()
        pr.enable()
        res = parser.parse_file(filename)
        parser.to_csv(res, outfile)
        pr.disable()
        pr.print_stats(sort="calls")


if __name__ == "__main__":
    unittest.main()