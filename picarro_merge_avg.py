#author: SAURABH ANNADATE

import pandas as pd
import glob
import os

path = '/media/vsinha/HP v301w/New folder/PICCARO/July/'
arr = os.listdir(path)
all_files = []
for i in arr:
	all_files = all_files + glob.glob(path+i + "/*.dat")
	
	
li = []

for filename in all_files:
    #frame = pd.read_csv(filename,sep='\t', encoding='cp1252',skiprows=9)  #ptrms
    frame = pd.read_csv(filename,sep="\s+")   #piccaro
    li.append(frame)
    
frame = pd.concat(li, axis=0, ignore_index=True)
#frame['datetime_ptrms'] = pd.to_datetime(frame['datetime_ptrms'])
#frame = frame.sort_values(by = 'datetime_ptrms')
frame['DATE_TIME'] = frame['DATE']+" "+ frame['TIME']
frame['DATE_TIME'] =  pd.to_datetime(frame['DATE_TIME'])
frame = frame.sort_values(by = 'DATE_TIME')
#frame.to_csv('merged_8feb_14july_picarro.csv')
piccaro_1min = frame.resample('1Min',on='DATE_TIME').mean()
piccaro_1min.to_csv('picarro_1minavg_july.csv')

