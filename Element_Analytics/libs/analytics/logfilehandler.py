""" 
This module processes csv's file and return a 
pandas dataframe for analytics module to work with
"""
import libs.utilities.pathtools as pt
import os
import pandas as pd
import tabulate

def read_log(username, log_name):
     """ Read a csv log and turn it in to pandas data frame"""
     log_path = pt.get_log_dir_abs(username, log_name + ".csv")
     if not os.path.isfile(log_path):
          raise LogNotFoundException
     
     frame = pd.read_csv(log_path, parse_date=True, encoding='utf-8', error_bad_lines=False)
     print(tabulate(frame, header='keys', tablefmt='psql'))

class LogNotFoundException(Exception):
     def __init__(self,  message, path):
          super().__init__(message)
          self.path = path