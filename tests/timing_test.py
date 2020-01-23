import sys
sys.path.append("..")
sys.path.append("../anomaly_detection/")

import timeit
import pandas as pd, numpy as np


def get_test_value(raw_value):
    return np.float64(raw_value)
  
def dparserfunc(date):
    return pd.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

data1 = pd.read_csv('test_data_1.csv', index_col='timestamp',
               parse_dates=True, squeeze=True,
               date_parser=dparserfunc)

data2 = pd.read_csv('test_data_2.csv', index_col='timestamp',
               parse_dates=True, squeeze=True,
               date_parser=dparserfunc)

data3 = pd.read_csv('test_data_3.csv', index_col='timestamp',
               parse_dates=True, squeeze=True,
               date_parser=dparserfunc)        


setup = '''
from anomaly_detection.anomaly_detect_ts import _detect_anoms, anomaly_detect_ts, \
    _get_data_tuple, _get_max_outliers, _get_max_anoms, _get_decomposed_data_tuple, \
    _perform_threshold_filter, _get_plot_breaks, _get_only_last_results, _get_period, \
    _get_dask_series
import pandas as pd
'''


def time_anomaly_detection():

    code = '''
  
def dparserfunc(date):
    return pd.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

data = pd.read_csv('test_data_1.csv', index_col='timestamp',
               parse_dates=True, squeeze=True,
               date_parser=dparserfunc)
anomaly_detect_ts(raw_data=data, direction='both', alpha=0.05, plot=False, longterm=True)    
'''

    # timeit.repeat statement 
    times = timeit.timeit(setup=setup, 
                      stmt=code, 
                      number = 5) 

    # priniting minimum exec. time 
    print('analytic execution time: {}'.format(times/5))  
    
    
def time_anomaly_detection_multithreaded():

    code = '''
  
def dparserfunc(date):
    return pd.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

data = pd.read_csv('test_data_1.csv', index_col='timestamp',
               parse_dates=True, squeeze=True,
               date_parser=dparserfunc)
anomaly_detect_ts(raw_data=data, direction='both', alpha=0.05, plot=False, longterm=True, multithreaded=True)    
'''

    # timeit.repeat statement 
    times = timeit.timeit(setup=setup, 
                      stmt=code, 
                      number = 5) 

    # priniting minimum exec. time 
    print('analytic execution time: {}'.format(times/5))  


if __name__ == "__main__": 
    time_anomaly_detection()
    print('###############################################')
    print('###############################################')
    time_anomaly_detection_multithreaded()
