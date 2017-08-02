# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:32:02 2017

@author: wangq
"""
import pandas as pd
import pylab
from pandas import Series, DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
result = DataFrame()
name_list = []
for file_index in range(11):
    temp_path = "Data-trials-"+str(file_index)+".csv"
    temp_data = pd.read_csv(temp_path, parse_dates=True,index_col=0) # Intron name at col 3 
    temp = temp_data["#outputs"]
    name_list.append("T-"+str(file_index))
    result = pd.concat([result,temp],axis=1)

result.columns = name_list
sns.heatmap(result,annot=True,linewidths=0.25)
pylab.savefig("heatmap-threshold.png")
f,(axis1,axis2) = plt.subplots(2,1)

yearly_flights = result.sum()

years = pd.Series(yearly_flights.index.values)
years = pd.DataFrame(years)

flights = pd.Series(yearly_flights.values)
flights = pd.DataFrame(flights)

year_dframe = pd.concat((years,flights),axis=1)
year_dframe.columns = ['Threshold','outputs']

ax = sns.barplot('Threshold',y='outputs',data=year_dframe,ax=axis1)

sns.heatmap(result,cmap='Blues',ax=axis2,cbar_kws={'orientation':'horizontal'})
ax.set(xlabel='')

pylab.savefig("heatmap-threshold2.png")