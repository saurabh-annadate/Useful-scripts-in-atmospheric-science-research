#author: Saurabh Annadate
import pandas as pd

PTRMS = pd.read_csv('ptrms_data.csv',skiprows=9)  #load ptc or csv
PTRMS['datetime_ptrms'] = pd.to_datetime(PTRMS['datetime_ptrms'],dayfirst=True)
PTRMS = PTRMS.set_index('datetime_ptrms')
PTRMS_4min = PTRMS.resample('4T').mean()
PTRMS_4min.to_csv('ptrms_4minavg.csv')
