import unittest
import time
import libs.parser.logparser as parser


class TestPerformance(unittest.TestCase):
    def test_parser(self):
        filename = input("Filename: ")
        outfile = input("Output file: ")

        print("Processing...\n")
        start = time.time()
        res = parser.parse_file_parallel(filename)
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


if __name__ == "__main__":
    unittest.main()