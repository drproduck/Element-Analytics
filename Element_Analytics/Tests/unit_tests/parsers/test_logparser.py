import libs.parser.logparser as parser
import pprint
import time

#Initial test. Performance ~ 24s for 100,000 log entries

pp = pprint.PrettyPrinter(indent=4, compact=True)

file = "./test_log"

start_time = time.time()
# res = parser.parse_dict_of_lists(file)
res = parser.parse_list_of_dicts(file)
elapsed_time = time.time() - start_time

print("Elapse time: ", elapsed_time)

for item in res:
    pp.pprint(item)
    print()

