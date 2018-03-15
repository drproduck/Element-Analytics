import libs.parser.logparser as parser
import pprint
import time

#Initial test. Performance ~ 24s for 100,000 log entries

pp = pprint.PrettyPrinter(indent=4)

file = "./test_log"
start_time = time.time()
res = parser.parse(file)
elapsed_time = time.time() - start_time
print("Elapse time: ", elapsed_time)
pp.pprint(res)

