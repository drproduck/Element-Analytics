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
    def test_parser(self):
        filename = input("Filename: ")
        outfile = input("Output file: ")

        #print("Processing...\n")
        #start = time.time()

        pr = cProfile.Profile()
        pr.enable()
        res = parser.parse_file(filename)
        pr.disable()
        # after your program ends
        pr.print_stats(sort="calls")


        #elapsed_time = time.time() - start
        #print("Process time: ", elapsed_time, "\n")
        #self.assertLess(elapsed_time, 60)

        #print("Writing CSV...\n")
        #start = time.time()
        parser.to_csv(res, outfile)
        #elapsed_time = time.time() - start
        #print("Write time: ", elapsed_time, "\n")
        #self.assertLess(elapsed_time, 30)

        #print("# of log entries processed: ", len(res))


if __name__ == "__main__":
    unittest.main()