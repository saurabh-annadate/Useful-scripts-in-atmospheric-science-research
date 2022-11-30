#author: Saurabh Annadate
import pandas as pd
import glob
import os

path = ''  #path to the folder consisting daywise folders of the PICARRO data
arr = os.listdir(path)
all_files = []                # list of all the data files need to merged
for i in arr:
	all_files = all_files + glob.glob(path+i + "/*.ptc")
		
li = []    # list for Picarro files as pandas dataframes

#data = pd.read_csv(all_files[0],sep='\t',encoding= 'unicode_escape',skiprows= 9)
#print(data)

for filename in all_files:
    frame = pd.read_csv(filename,sep='\t',encoding= 'unicode_escape',skiprows= 9)   #ptrms
    li.append(frame)
    
frame = pd.concat(li, axis=0, ignore_index=True)  #concatanate all separate dataframes into one dataframe

frame['datetime_ptrms'] =  pd.to_datetime(frame['datetime_ptrms']) #read it as pandas datetime format
frame = frame.sort_values(by = 'datetime_ptrms')  #sort the dataframe by DATE_TIME
#frame.to_csv('merged_picarro.csv')
ptrms_4min = frame.resample('4Min',on='datetime_ptrms').mean() #4 minute average file
ptrms_4min.to_csv('ptrms_ptc_Nov_Aug.csv') #save as csv file
