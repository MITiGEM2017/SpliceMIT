# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:36:52 2017

@author: wangq
"""
from tqdm import *
import csv
fh = open("human.txt","r")

info_list = fh.readlines()


seq = []

for line in tqdm(info_list):
    if line[0] != ">" and len(line)>0:
        seq.append(line[:-1])

with open('human-cDNA.csv','w',newline='') as fp:
    a = csv.writer(fp,delimiter=',')
    a.writerows(seq)

