# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:52:30 2017

@author: wangq
"""

def GC_content(gRNA_seq):
    return round((gRNA_seq.upper().count("C")+gRNA_seq.upper().count("G"))/(len(gRNA_seq)),3), gRNA_seq.upper().count("G")/len(gRNA_seq)

