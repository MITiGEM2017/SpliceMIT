# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:43:49 2017

@author: wangq
"""
# %matplotlib inline
import csv
import numpy as np
import pandas as pd
import pylab
from pandas import Series, DataFrame

from numpy.random import randn

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv", parse_dates=True)

sns.lmplot("Intron Size","#outputs", data, scatter_kws={'marker':'o','color':'indianred'},line_kws={'linewidth':1,'color':'blue'})
pylab.savefig('Intron size vs. outputs correlation.png')
sns.jointplot("Intron Size","#outputs", data, kind="kde")
pylab.savefig('Intron size vs. outputs jointplot.png')
sns.jointplot("Intron Size","#outputs", data, kind="resid",color="indianred")
pylab.savefig("Intron vs. outputs residues.png")
sns.jointplot("Intron Size", "#outputs",data,kind="reg",order=1)
pylab.savefig("Intron vs. outputs regression.png")
##sns.lmplot("GC Content","#outputs", data, scatter_kws={'marker':'o','color':'indianred'},line_kws={'linewidth':1,'color':'blue'})
##sns.jointplot("GC Content","#outputs", data, kind="kde")

##sns.lmplot("G%","#outputs", data, scatter_kws={'marker':'o','color':'indianred'},line_kws={'linewidth':1,'color':'blue'})
##sns.jointplot("G%","#outputs", data, kind="kde",color="indianred")
#sns.kdeplot(data["#outputs"])
#sns.kdeplot(data["G%"])
#sns.kdeplot(data["GC Content"])
