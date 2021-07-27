#author: SAURABH ANNADATE

import pandas as pd
import glob
import os

path = '/home/PICARRO/July/'  #path to the folder consisting daywise folders of the PICARRO data
arr = os.listdir(path)
all_files = []                # list of all the data files need to merged
for i in arr:
	all_files = all_files + glob.glob(path+i + "/*.dat")
	
	
li = []    # list for Picarro files as pandas dataframes

for filename in all_files:
    frame = pd.read_csv(filename,sep="\s+")   #piccaro
    li.append(frame)
    
frame = pd.concat(li, axis=0, ignore_index=True)  #concatanate all separate dataframes into one dataframe

frame['DATE_TIME'] = frame['DATE']+" "+ frame['TIME']  #merge DATE and TIME columns to DATE_TIME
frame['DATE_TIME'] =  pd.to_datetime(frame['DATE_TIME']) #read it as pandas datetime format
frame = frame.sort_values(by = 'DATE_TIME')  #sort the dataframe by DATE_TIME
#frame.to_csv('merged_picarro.csv')
piccaro_1min = frame.resample('1Min',on='DATE_TIME').mean() #1 minute average file
piccaro_1min.to_csv('picarro_1minavg_july.csv') #save as csv file

