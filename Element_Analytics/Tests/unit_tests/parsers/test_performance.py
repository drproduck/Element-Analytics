import unittest
import time
import libs.parser.logparser as parser


class TestPerformance(unittest.TestCase):
    def test_performance(self):
        filename = input("Filename: ")
        start = time.time()
        res = parser.parse_file_parallel(filename or "/home/lynux/workspace/Element-Analytics/logs/xaa")
        elapsed_time = time.time() - start
        self.assertLess(elapsed_time, 60)
        print(len(res))
        print(elapsed_time)


if __name__ == "__main__":
    unittest.main()