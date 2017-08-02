# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:46:53 2017

@author: wangq
"""

import pandas as pd
import numpy as np
import pylab
from pandas import Series, DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

def bigger(a,b):
    if a > b:
        return a
    return b

def smaller(a,b):
    if a < b:
        return a
    return b

data = pd.read_csv("Output_methods_comparison.csv")
pair_plot_df = DataFrame()

"""Cutoff vs weighted"""
prob_cutoff_weighted_list = []
for index in range(data.intron_size.count()):
    temp = bigger(data.overlap_cutoff_vs_weighted[index]/data.cutoff_output[index],data.overlap_cutoff_vs_weighted[index]/data.weighted_output[index])
    temp = round(temp,2)
    if temp == 0 and (data.cutoff_output[index] < 5 or data.weighted_output[index] < 5):
        prob_cutoff_weighted_list.append(np.nan)
    else:
        prob_cutoff_weighted_list.append(temp)

data['percent_cutoff_vs_weighted'] = prob_cutoff_weighted_list
pair_plot_df['percent_cutoff_vs_weighted'] = Series(prob_cutoff_weighted_list).dropna()


"""Cutoff vs rank product"""
prob_cutoff_rp_list = []
for index in range(data.intron_size.count()):
    temp = bigger(data.overlap_cutoff_vs_rp[index]/data.cutoff_output[index],data.overlap_cutoff_vs_rp[index]/data.rp_output[index])
    temp = round(temp,2)
    if temp == 0 and (data.cutoff_output[index] < 5 or data.rp_output[index] < 5):
        prob_cutoff_rp_list.append(np.nan)
    else:
        prob_cutoff_rp_list.append(temp)
    

data['percent_cutoff_vs_rp'] = prob_cutoff_rp_list
pair_plot_df['percent_cutoff_vs_rp'] = Series(prob_cutoff_rp_list).dropna()


"""Weighted vs rank product"""
prob_rp_weighted_list = []
for index in range(data.intron_size.count()):
    temp = bigger(data.overlap_rp_vs_weighted[index]/data.rp_output[index],data.overlap_rp_vs_weighted[index]/data.weighted_output[index])
    if temp == 0 and (data.weighted_output[index] < 5 or data.rp_output[index] < 5):
        prob_rp_weighted_list.append(np.nan)
    else:
        prob_rp_weighted_list.append(temp)

data['percent_rp_vs_weighted'] = prob_rp_weighted_list
pair_plot_df['percent_rp_vs_weighted'] = Series(prob_rp_weighted_list).dropna()
pair_plot_df['GC_content'] = data["GC_content"]


sns.pairplot(pair_plot_df)

g = sns.PairGrid(pair_plot_df)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, cmap="Blues_d", n_levels=6)

"""
Separation Zone

"""
# Distribution graph of RP vs weighted
plt.figure(figsize=(12,8))
plt.title('Distribution of Rank-product vs Weighted')
plt.xlabel('Percent of Overlap')
plt.ylabel('Frequency [%]')

ax = (data.percent_rp_vs_weighted.value_counts()/len(data.percent_rp_vs_weighted.dropna())*100).sort_index().plot(kind="bar", rot=0)
ax.set_yticks(np.arange(0, 110, 10))

ax2 = ax.twinx()
ax2.set_yticks(np.arange(0, 110, 10)*len(data)/100)

for p in ax.patches:
    ax.annotate('{:.2f}%'.format(p.get_height()), (p.get_x()+0.15, p.get_height()+1))
    

"""
Separation Zone

"""
# Distribution graph of cutoff vs Rank-Product
plt.figure(figsize=(12,8))
plt.title('Distribution of Cutoff vs Rank-Product')
plt.xlabel('Percent of Overlap')
plt.ylabel('Frequency [%]')

ax = (data.percent_cutoff_vs_rp.value_counts()/len(data.percent_cutoff_vs_rp.dropna())*100).sort_index().plot(kind="bar", rot=0)
ax.set_yticks(np.arange(0, 110, 10))

ax2 = ax.twinx()
ax2.set_yticks(np.arange(0, 110, 10)*len(data)/100)

for p in ax.patches:
    ax.annotate('{:.2f}%'.format(p.get_height()), (p.get_x()+0.15, p.get_height()+1))
    
"""
Separation Zone

"""
# Distribution graph of cutoff vs weighted
plt.figure(figsize=(12,8))
plt.title('Distribution of Cutoff vs Weighted')
plt.xlabel('Percent of Overlap')
plt.ylabel('Frequency [%]')

ax = (data.percent_cutoff_vs_weighted.value_counts()/len(data.percent_cutoff_vs_weighted.dropna())*100).sort_index().plot(kind="bar", rot=0)
ax.set_yticks(np.arange(0, 110, 10))

ax2 = ax.twinx()
ax2.set_yticks(np.arange(0, 110, 10)*len(data)/100)

for p in ax.patches:
    ax.annotate('{:.2f}%'.format(p.get_height()), (p.get_x()+0.15, p.get_height()+1))