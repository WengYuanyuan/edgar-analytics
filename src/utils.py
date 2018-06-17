import sys
import os
from glob import glob
import csv
from datetime import datetime
import time
import argparse

def get_requests_log(logfile_name):
    '''
    A generator for the data in log.csv. Since csv files can contain over 10 
    millions of records, it is not necessary to store all the record in memory
    all at once.
    Input: csv_fname:
        filename/location of the csv.
    Output: log_record    
    ''' 
    with open(logfile_name, "r") as request_logs:
        for request_log in csv.reader(request_logs, delimiter=','):
          yield request_log
          
def check_request(row):
    '''
    Helper function to check if each record has the missing information or not
    Input: row from readint the csv
    Output: True or False
    '''
    if len(row[0])>0 and len(row[1])>0 and len(row[2])>0 and len(row[4])>0 and len(row[5])>0 and len(row[6])>0:
          return True
    else:
          return False

