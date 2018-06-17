import sys
import os
from glob import glob
import csv
from datetime import datetime
import time
import argparse

from pqdict import pqdict

from utils import get_requests_log, check_request
          
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
     
if __name__ == '__main__':  
    
    inactive_period = open('/Users/quanquan/Documents/insight2/edgar-analytics/insight_testsuite/tests/test_1/input/inactivity_period.txt','r')
    inact_period = float(inactive_period.read()[0])
    
    
    output_file = open('/Users/quanquan/Documents/insight2/edgar-analytics/insight_testsuite/tests/test_1/output/sessionization.txt', 'w')
    requests = iter(get_requests_log('/Users/quanquan/Documents/insight2/edgar-analytics/insight_testsuite/tests/test_1/input/log.csv'))
    # ingore the head line
    next(requests, None) 
         
    # use dictionary to track necessary information of currently active sessions.
    dict_ip_sess = {}
    
    # initialize 'indexed' priority queue 
    # for each session, the earlier time_stamp of the last request, the higher priority
    # 'indexed' priority queue updates the time_stamp of last request in O(1) time (which also needs O(log(n)) to rebuilt heap
    pd = pqdict({})
    

    for (i, req)  in enumerate(requests): 
        # ingore the empty record
        if not check_request(req):
            continue
            
        ip = req[0] 

        req_time = req[1] + " " + req[2]
        req_time = datetime.strptime(req_time, "%Y-%m-%d %H:%M:%S")
        
        # initialize the starting time 
        if i==0:
            start = time.mktime(req_time.timetuple())
            prev = 0.0
    
        # get time of current request record  
        cur = time.mktime(req_time.timetuple()) 
        cur -= start
        
        # for a new timestamp, check if there is any session expired: 
        # delete the session if expired
        # update session record(dict and pd) if not expired
        if cur > prev:
            while len(pd) > 0:
                if pd.topitem()[1] + inact_period + 1 > cur:
                    break
                temp_ip = pd.pop()
                output_file.write("%s\n" % tuple_to_str(dict_ip_sess[temp_ip], temp_ip, start))
                dict_ip_sess.pop(temp_ip, None)
        if ip not in dict_ip_sess:
            counter = 1
            dict_ip_sess[ip] = (cur, cur, counter)
            pd[ip] = cur
        else:
            temp = dict_ip_sess[ip]
            dict_ip_sess[ip] = (temp[0], cur, temp[2]+1)
            pd[ip] = cur
        prev = cur
            
    for key in pd:
        pd[key]=dict_ip_sess[key][0]
    
    while len(pd)>0:
        temp_ip = pd.pop()
        output_file.write("%s\n" % tuple_to_str(dict_ip_sess[temp_ip], temp_ip, start))
   
    output_file.close()  
    
