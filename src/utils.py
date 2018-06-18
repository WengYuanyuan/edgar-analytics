import csv
from datetime import datetime


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

def tuple_to_str(record, ip, start_time):
     '''
      A helper funciton that converts dictionary entry to string for output file
     Input:
        tup: dictionary value in tuple
        key: dictionary key
        t_base: starting timestamp as a base
     Return:
        rslt_str: string in the required format
     '''
     start, end = record[0] + start_time, record[1] + start_time
     start, end = datetime.fromtimestamp(start), datetime.fromtimestamp(end)
     dt_str = str(int(record[1] - record[0]+1))
     counts = str(record[2])
     output = ip+','+str(start)+','+str(end)+','+dt_str+',' + counts
     return output

