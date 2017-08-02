# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:50:38 2017

@author: wangq
"""

cutoff_GC_content = 0
cutoff_off_target = 20
cutoff_RBP = 1e10                        
cutoff_gRNA = 0.0005                     
cutoff_pre_crRNA = 0.0005

bool_list = []
index_list =[]
print ("Final filter of the gRNAs in process: ")
for n in tqdm(range(len(gRNA_seq_list))):
    if (GC_content_score_list[n] <= cutoff_GC_content and off_target_score_list[n] <= cutoff_off_target and RBP_competition_score_list[n] <= cutoff_RBP and Nupack_gRNA_final_score[n] >= cutoff_gRNA and pre_crRNA_structure_score_list[n] >= cutoff_pre_crRNA):
        bool_list.append(True)
        index_list.append(n)
    else:
        bool_list.append(False)
"""
for index in index_list:
    print("\n")
    print("Secondary structure score:  ",Nupack_gRNA_final_score[index])
    print("Pre-crRNA secondary structure score:  ",pre_crRNA_structure_score_list[index])
    print("RBP intereference score:  ", RBP_competition_score_list[index])
    print("GC Content penalty score:  ",GC_content_score_list[index])
    print("Off target penalty score:  ",off_target_score_list[index])
""" 
print(len(index_list))