# -*- coding: utf-8 -*-
"""
Created on Wed Jun 3 14:59:28 2017

@author: Qianchang Dennis Wang
"""

# All packages

import sys
import ast
import re
import csv
import time
import math
import numpy as np
from scipy import stats
from timeit import default_timer as timer
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import *


"""
Sample Intron sequence: GTGAGTCTATGGGACCCTTGATGTTTTCTTTCCCCTTCTTTTCTATGGTTAAGTTCATGTCATAGGAAGGGGAGAAGTAACAGGGTACAGTTTAGAATGGGAAACAGACGAATGATTGCATCAGTGTGGAAGTCTCAGGATCGTTTTAGTTTCTTTTATTTGCTGTTCATAACAATTGTTTTCTTTTGTTTAATTCTTGCTTTCTTTTTTTTTCTTCTCCGCAATTTTTACTATTATACTTAATGCCTTAACATTGTGTATAACAAAAGGAAATATCTCTGAGATACATTAAGTAACTTAAAAAAAAACTTTACACAGTCTGCCTAGTACATTACTATTTGGAATATATGTGTGCTTATTTGCATATTCATAATCTCCCTACTTTATTTTCTTTTATTTTTAATTGATACATAATCATTATACATATTTATGGGTTAAAGTGTAATGTTTTAATATGTGTACACATATTGACCAAATCAGGGTAATTTTGCATTTGTAATTTTAAAAAATGCTTTCTTCTTTTAATATACTTTTTTGTTTATCTTATTTCTAATACTTTCCCTAATCTCTTTCTTTCAGGGCAATAATGATACAATGTATCATGCCTCTTTGCACCATTCTAAAGAATAACAGTGATAATTTCTGGGTTAAGGCAATAGCAATATTTCTGCATATAAATATTTCTGCATATAAATTGTAACTGATGTAAGAGGTTTCATATTGCTAATAGCAGCTACAATCCAGCTACCATTCTGCTTTTATTTTATGGTTGGGATAAGGCTGGATTATTCTGAGTCCAAGCTAGGCCCTTTTGCTAATCATGTTCATACCTCTTATCTTCCTCCCACAG
sample test intron: gtaagttgcccagcagctcttagcattgaagaagttggttcttaaacatgaatccatgattgaaaaatggtttctgtggtcttaggtttcagaagtctgaaataccagtatcctgtaaggattatttgaattgaattagagtataaagtctactttttgtctttatttttaacaggaatttccttcatgtgtatattatgtagaaggaagtactgcaagaagtacacaggctttcaggctgaaagttttcatcttgattatgtttggcccatgactttttcattttgggagacaacaagggagtccatggcgcaaaaatgctgacatgtgttttttagctttggaagctaggcgtttcctacggtctcgcgataataaatgtgctcataaaacccatgacctagaatggggaatttctgtcattcatgagtatcatggcttacttttcgttgttgtagttaatgaagaattcctaattctttaaaatttataatactgtataattttgttttttaatacacattgttag    
upstream exon sequence (20 nt): ccttcatcaaccacacccag
downstream exon sequence (20 nt): ggcttcacctgggaaagagt
"""

def gRNA_length_input():
    t = True
    while t:
        l = int(input("Please input your desired gRNA length. The range is 18 to 28.  ----->    "))
        if (l >= 18 and l <= 28):
            t = False
        else:
            print ("Invalid input. Not in range. ")

    return l

def intron_input():
    t = True
    AUCG_test = True
    while t and AUCG_test:
        seq = input('Please input your intron sequence...   ')
        seq = seq.upper()
        if len(seq)<26:
            print("Invalid input. [Length of the intron invalid]")
        elif (seq[:2]!="GT" or seq[len(seq)-2:]!="AG"):
            print("Invalid input. [Conserved sequence invalid]")
        else:
            num = 0
            while num<len(seq):
                if seq[num] not in 'ATCG':
                    print("Invalid input. [Nucleotides other than A,T,C,G]")
                    print("Invalid base position:",num)
                    num=100000
                else:
                    num+=1

            if num != 100000:
                print ("\n")
                print("Your input intron sequence is",seq)
                t=False
                AUCG_test = False
    print ("The length of the intron is ",len(seq))
    return seq


def upstream_exon_input():
    t = True
    AUCG_test = True
    while t and AUCG_test:
        seq = input('Please input your upstream 20nt exon sequence...   ')
        seq = seq.upper()
        if len(seq) != 20:
            print("Invalid input. [Length invalid - should be 20]")
        else:
            num = 0
            while num<len(seq):
                if seq[num] not in 'ATCG':
                    print("Invalid input. [Nucleotides other than A,T,C,G]")
                    print("Invalid base position:",num)
                    num=100000
                else:
                    num+=1

            if num != 100000:
                print("Your input upstream exon sequence is",seq)
                t=False
                AUCG_test = False
    return seq


def downstream_exon_input():
    t = True
    AUCG_test = True
    while t and AUCG_test:
        seq = input('Please input your downstream 20nt exon sequence...   ')
        seq = seq.upper()
        if len(seq) != 20:
            print("Invalid input. [Length invalid - should be 20]")
        else:
            num = 0
            while num<len(seq):
                if seq[num] not in 'ATCG':
                    print("Invalid input. [Nucleotides other than A,T,C,G]")
                    print("Invalid base position:",num)
                    num=100000
                else:
                    num+=1

            if num != 100000:
                print("Your input downstream exon sequence is",seq)
                t=False
                AUCG_test = False

    return seq


def start_site(seq,gRNA_len):
    site=[]
    pos = 0

    while pos<(len(seq)-gRNA_len):
        signal = True
        if(seq[pos+gRNA_len]=="G"):
            signal = False

        if(signal):
            site.append(pos)
        pos+=1
    #print (site)
    return site
    #return the available start site of guide RNA



"""
Produce gRNA in a list
Could be traced with position number
"""

#Tiling
def gen_gRNA_seq(seq,site,gRNA_len):
    gRNA_list = []
    for gRNA_pos in site:
        temp = ""+tracrRNA_seq
        for num in range(gRNA_len):
            position = num+gRNA_pos-1
            base = seq[position]
            index = "ATCG".find(base)
            complement = "UAGC"[index]
            temp += complement
        gRNA_list.append(temp)
    #return a list containing all the guide RNA sequences
    print ("The number of guide RNA sequences is ",len(gRNA_list))
    #Count the number of the gRNA sequences - for test use
    return gRNA_list



def diff_letters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )


def off_target_mismatch(mRNA,gRNA_seq):
    crRNA_seq = gRNA_seq[-gRNA_length:]

    count = 0
    difference_list = []
    RNA_complement = ""
    for num in range(len(crRNA_seq)):
        base = crRNA_seq[num]
        index = "UAGC".find(base)
        complement = "ATCG"[index]
        RNA_complement += complement

    for mRNA_seq in mRNA:
        start_pos = 0
        while start_pos < (len(mRNA_seq)-len(crRNA_seq)+1):
            DNA_seq = mRNA_seq[start_pos:(start_pos+len(crRNA_seq))]
            diff = diff_letters(RNA_complement, DNA_seq)
            if diff <= off_target_mismatch_threshold:
                count +=1
                difference_list.append(diff)
                start_pos += 1

            else:
                start_pos += (diff-off_target_mismatch_threshold)

    return count, difference_list


def remove_values_from_list(the_list, val):
    while val in the_list:
        the_list.remove(val)


def RBP_data_scrap(analyze_seq):
    # RBPmap mapping binding sites of RNA bindinG proteins
    # "http://rbpmap.technion.ac.il/"
    RBP_driver = webdriver.PhantomJS()
    RBP_driver.get("http://rbpmap.technion.ac.il/")

    mRNA_input = analyze_seq


    # The following is to find the text field and input sequence
    mRNA_input_Xpath = "//textarea"
    mRNA_input_Field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(mRNA_input_Xpath))
    mRNA_input_Field.clear()
    mRNA_input_Field.send_keys(mRNA_input)
    # send the input in the text box


    mode_Xpath = "//*[@id=\"motifs_block\"]/div[1]/div[2]/div[2]/input[1]"
    mode_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(mode_Xpath))
    mode_field.click()
    # click the mode selection


    click_here_Xpath = "//*[@id=\"motifs_block\"]/div[1]/div[2]/div[2]/a"
    click_here_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(click_here_Xpath))
    click_here_field.click()
    #click the "click here" button


    RBP_driver.switch_to_window(RBP_driver.window_handles[1])
    choose_RBP_Xpath = "/html/body/form/table/tbody/tr[2]/td/div[1]/input"
    choose_RBP_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(choose_RBP_Xpath))
    choose_RBP_field.click()
    # click the "Human" RBPs in the new window


    submit_RBP_Xpath = "/html/body/form/table/tbody/tr[4]/td/input"
    submit_RBP_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(submit_RBP_Xpath))
    submit_RBP_field.click()
    # click submit button


    RBP_driver.switch_to_window(RBP_driver.window_handles[0])
    submit_analysis_Xpath = "/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[6]/td/input[1]"
    #submit_analysis_Xpath = "(//input[@value])[14]"
    submit_analysis_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(submit_analysis_Xpath))
    submit_analysis_field.click()
    #click the submit button for the analysis

    print ("RNA binding protein site analysis in progress ------")
    print ("This process should take less than 1 minute.")
    view_result_Xpath = "/html/body/table/tbody/tr[2]/td[2]/div[8]/div[3]/a"
    view_result_field = WebDriverWait(RBP_driver,60).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(view_result_Xpath))
    print ("Process finished.")
    # waiting for the result for at most 1 minute(s), could be modified
    view_result_field.click()


    table_Xpath = "(//table)[3]"
    RBP_initial_table = WebDriverWait(RBP_driver,30).until(lambda RBP_driver: RBP_driver.find_elements_by_xpath(table_Xpath))
    RBP_rearranged_table = [x.text for x in RBP_initial_table][0]  # String we want
    nicer_table = RBP_rearranged_table.split("\n")
    remove_values_from_list(nicer_table, 'Position Motif Occurrence Z-score P-value')


    count = 0
    final_table = []
    nicer_table.append("xxx")
    while count<(len(nicer_table)):
        reading = nicer_table[count]
        temp = ""
        if reading[:7] == "Protein":
            temp += (reading[:8] + reading[9:])
            inner_count = 1
            while (nicer_table[inner_count+count][:7] != "Protein"):
                if(inner_count+count)<(len(nicer_table)-1):
                    add_content = temp+" "+nicer_table[inner_count+count]
                    final_table.append(add_content)
                    inner_count +=1
                else:
                    break

        #final_table.append(temp)
        #print (temp)
        count += inner_count

    ult_table = []
    for data_string in final_table:
        temp = data_string.split()
        del temp[3]
        temp.append(len(temp[2]))  # add a column containing length of the motif
        temp[0] = temp[0][8:-7]
        temp[1] = int(temp[1]) - len(upstream_exon)
        temp[3] = float(temp[3])
        temp[4] = float(temp[4])
        temp.append((len(temp[2])+temp[1]-1)) # add a colum containing the end position of the motif
        ult_table.append(temp)
        
    RBP_driver.quit()    
    
    return ult_table


# Function used to extract the dissociation constant for a given RBP name and the data_list
def extract_RBP_Kd(RBP_Kd_list, RBP_name):
    for each_RBP in RBP_Kd_list:
        if(each_RBP[0]==RBP_name):
            return float(each_RBP[1])
    return False


#RBP score calculation tool
def RBP_competition_score(site,gRNA_seq,gRNA_list,RBP_data_list,RBP_Kd_list):
    start_pos = site[gRNA_list.index(gRNA_seq)]
    end_pos = start_pos + gRNA_length -1
    potential_RBP_list = []
    partial_RBP_list = []

    for row in RBP_data_list:
        if (row[1]<=end_pos and row[1]>=start_pos):
            if(row[-1]<=end_pos):
                potential_RBP_list.append(row)
            else:
                partial_RBP_list.append(row)
        elif (row[-1]>=start_pos and row[1]<start_pos):
            partial_RBP_list.append(row)


    sum_RBP_interference_score = 0  # return value

    # For the score from RBPs that completely bind in the region
    sum_complete_bind = 0
    RBP_num_count = 0
    while RBP_num_count < len(potential_RBP_list):
        potential_info_list = potential_RBP_list[RBP_num_count]
        potential_start_pos = potential_info_list[1]
        potential_RBP_test = True
        power_count = 0
        base_score = 0
        if extract_RBP_Kd(RBP_Kd_list,potential_info_list[0]) != 0:
            base_score = (1/extract_RBP_Kd(RBP_Kd_list,potential_info_list[0]))
        complete_score_list = []
        complete_score_list.append(base_score)
        while (potential_RBP_test and (RBP_num_count+power_count+1)<len(potential_RBP_list)):
            if(potential_RBP_list[RBP_num_count+power_count+1][1] == potential_start_pos):
                power_count += 1
                potential_info_list = potential_RBP_list[RBP_num_count+power_count]
                additional_score = ((1-potential_info_list[4])**binding_prob_power)*extract_RBP_Kd(RBP_Kd_list,potential_info_list[0])  #temporary score
                complete_score_list.append(additional_score)
            else:
                potential_RBP_test = False
                RBP_num_count += power_count


        if len(complete_score_list) > 1:
            while len(complete_score_list) > 1:
                minimum_score = min(complete_score_list)
                sum_complete_bind += minimum_score*(weighted_factor**power_count)
                power_count -= 1
                complete_score_list.remove(minimum_score)

        else:
            sum_complete_bind += base_score


        RBP_num_count += 1



    # Score for partially bind RBPs in the region
    sum_partially_bind = 0
    RBP_num_count = 0
    while RBP_num_count < len(partial_RBP_list):
        potential_info_list = partial_RBP_list[RBP_num_count]
        potential_start_pos = potential_info_list[1]
        potential_RBP_test = True
        power_count = 0
        factor = min((potential_info_list[6]-start_pos+1),(end_pos-potential_info_list[1]+1))/potential_info_list[5]
        base_score = ((1-potential_info_list[4])**binding_prob_power)*extract_RBP_Kd(RBP_Kd_list,potential_info_list[0])*factor
        complete_score_list = []
        complete_score_list.append(base_score)
        while (potential_RBP_test and (RBP_num_count+power_count+1)<len(partial_RBP_list)):
            if(partial_RBP_list[RBP_num_count+power_count+1][1] == potential_start_pos):
                power_count += 1
                potential_info_list = partial_RBP_list[RBP_num_count+power_count]
                factor = min((potential_info_list[6]-start_pos+1),(end_pos-potential_info_list[1]+1))/potential_info_list[5]
                additional_score = ((1-potential_info_list[4])**binding_prob_power)*extract_RBP_Kd(RBP_Kd_list,potential_info_list[0])*factor  #temporary score
                complete_score_list.append(additional_score)
            else:
                potential_RBP_test = False
                RBP_num_count += power_count

        if len(complete_score_list) > 1:
            while len(complete_score_list) > 1:
                minimum_score = min(complete_score_list)
                sum_partially_bind += minimum_score*(weighted_factor**power_count)
                power_count -= 1
                complete_score_list.remove(minimum_score)
        else:
            sum_partially_bind += base_score

        RBP_num_count += 1

    sum_RBP_interference_score = sum_partially_bind+sum_complete_bind


    return sum_RBP_interference_score



# Nupack
#"http://www.nupack.org/partition/new"
# Secondary Structure analysis

def Nupack_data_scrap(gRNA_seq,hp_driver):
    
    hp_driver.get("http://www.nupack.org/partition/new")

    # The following is to find the text field and input sequence
    gRNA_input_Xpath = "//textarea"
    gRNA_input_Field = WebDriverWait(hp_driver,30).until(lambda hp_driver: hp_driver.find_element_by_xpath(gRNA_input_Xpath))
    gRNA_input_Field.clear()
    gRNA_input_Field.send_keys(gRNA_seq)

    analyze_button_name = "commit"
    analyze_button_element = WebDriverWait(hp_driver,30).until(lambda hp_driver: hp_driver.find_element_by_name(analyze_button_name))
    analyze_button_element.click()

    switch_element = WebDriverWait(hp_driver,60).until(lambda hp_driver: hp_driver.find_element_by_id("dp"))
    switch_element.click()

    download_data_Xpath = "//*[@id=\"svg_link\"]/a[2]"
    download_data_element = WebDriverWait(hp_driver,30).until(lambda hp_driver: hp_driver.find_element_by_xpath(download_data_Xpath))
    download_data_element.click()

    data_elements = WebDriverWait(hp_driver,30).until(lambda hp_driver: hp_driver.find_elements_by_tag_name("body"))
    improved_data = [x.text for x in data_elements][0]
    better_table = improved_data.split("\n")
    better_table = better_table[13:]

    final_Nupack_gRNA_list =[]
    for line in better_table:
        temp = line.split()
        final_Nupack_gRNA_list.append(temp)


    #print ("It takes ",round(end-start)," seconds to finish the Nupack analysis for the sequence: ", gRNA_seq)
    return final_Nupack_gRNA_list




def Nupack_gRNA_score(final_Nupack_gRNA_list):
    Nupack_gRNA_score_list = []
    for each_gRNA_data in final_Nupack_gRNA_list:
        temp_list = each_gRNA_data[-gRNA_length:]  # Get the range of -22: ---> all containing individual probabilities of stem loop
        temp_product = 1

        for subset in temp_list:
            if (subset[1]=="-1"):
                prob = float(subset[2])
            else:
                prob = 0.001

            temp_product *= prob

        Nupack_gRNA_score_list.append(temp_product)

    return Nupack_gRNA_score_list



def gRNA_secondary_structure_score_weight(gRNA_2_score_list):
    maximum_score = max(gRNA_2_score_list)
    weight_power = (math.log(maximum_score,secondary_structure_score_prob_target))*(math.log10(maximum_score))
    final_gRNA_secondary_score_list = []
    for gRNA_2_score in gRNA_2_score_list:
        temp_score = gRNA_2_score**(math.log10(gRNA_2_score)/weight_power)
        final_gRNA_secondary_score_list.append(temp_score)

    return final_gRNA_secondary_score_list





# calculate the GC content of the givern sequence - sgRNA
def GC_content(gRNA_seq):
    return round((gRNA_seq.count("C")+gRNA_seq.count("G"))/(len(gRNA_seq)),3)







print ("The default setting for this program is not to have a log file.")
log_choice = input("Would you like to have a log file? ---- enter y to answer YES.        ")
log_judge = (log_choice.lower() == "y")




# Global Constant
#gRNA_length = 22                             # Used in two functions: RBP_competition_score, off_target_mismatch
intron_seq = intron_input()
tracrRNA_seq = "CCACCCCAAUAUCGAAGGGGACUAAAAC"
off_target_mismatch_threshold = 5            # Off-target mismatch nucleotides threshold, used in function: off_target_mismatch
weighted_factor = 0.4                        # weighted factor, used in RBP interference score calculation. Used in function: RBP_competition_score
binding_prob_power = 2                       # weighted factor, used in RBP interference score calculation. Used in function: RBP_competition_score
GC_threshold_low = 0.35                      # GC low threshold for a bad content
GC_threshold_high = 0.80                     # Above, high threshold
secondary_structure_score_prob_target = 0.95 # constant used in function: gRNA_secondary_structure_score_weight  range:[0.949,0.951]
GC_content_penalty_score = 1000              # Constant used in the coding part - GC analysis
direct_repeat_sequence = "CCACCCCAATATCGAAGGGGACTAAAAC"
                                             # set more mm score if needed
off_target_overwhelm = 3000                  # Score if number of off-target is more than 100
mm5_score = 10
mm4_score = 20                               # Score for mismatch with base difference: 4
mm3_score = 200                              # Score for mismatch with base difference: 3
mm2_score = 300                              # Score for mismatch with base difference: 2
mm1_score = 450                              # Score for mismatch with base difference: 1
mm0_score = 1000                              # Score for mismatch with base difference: 0
default_mm_score = 10                        # default score for mismatches with base difference more than 4

cutoff_GC_content = 0
cutoff_off_target = 10
cutoff_RBP = 9e7                        # Around 20 percent in test sample...
cutoff_gRNA = 0.01                      # Around 10 percent ...
cutoff_pre_crRNA = 0.01                 # Around 8 percent ...


# Start the log or not
if(log_judge):
    print ("The rest of the process would not be shown on the interface. Instead, it will be recorded as message.log in your working directory.")
    old_stdout = sys.stdout
    log_file = open("message.log","w")
    sys.stdout = log_file



# Where running codes start
gRNA_length = gRNA_length_input()
gRNA_start_site = start_site(intron_seq, gRNA_length)
upstream_exon = upstream_exon_input()
downstream_exon = downstream_exon_input()
gRNA_seq_list = gen_gRNA_seq(intron_seq, gRNA_start_site,gRNA_length)






# ----------------------------Separation Line--------------------------------



# ---------------------------------------------------------------------------



# ----------------------------Separation Line--------------------------------
# Nupack data for secondary structure begins here
gRNA_stats_list = []

# Following is for a separate run if no Nupack data locally
"""
print("\n")
print("Data scraping from Nupack for secondary structure of crRNA in progress:")
temp_driver = webdriver.Firefox()
for gRNA_sequence in tqdm(gRNA_seq_list):
    stats_list_secondary_structure = Nupack_data_scrap(gRNA_sequence,temp_driver)
    gRNA_stats_list.append(stats_list_secondary_structure)
temp_driver.quit()

with open('Nupack_data.csv','w',newline='') as fp:
    a = csv.writer(fp,delimiter=',')
    a.writerows(gRNA_stats_list)
"""

# Nupack Data for gRNA
# For the following, use it if the file exists. Otherwise, run the above codes to scrap data from Nupack and then save to this file name: Nupack_data.csv
print("\n")
print("Extract secondary structure data of crRNA from the csv file in progress:")
with open("Nupack_data.csv", "r") as nfile:
    nreader = csv.reader(nfile)
    for row in tqdm(nreader):
        gRNA_stats_list.append(row)
print("\n")
for each_gRNA in gRNA_stats_list:
    for data in each_gRNA:
        each_gRNA[each_gRNA.index(data)] = ast.literal_eval(data)

Nupack_gRNA_final_score = Nupack_gRNA_score(gRNA_stats_list)

# Final score for crRNA's secondary structure - variable: Nupack_gRNA_final_score
# ------------------------------Separation Line -----------------------------



# ---------------------------------------------------------------------------



# ------------------------------Separation Line -----------------------------
# RBP data and calculations:
# RBP data list from RBPmap
RBP_time1 = timer()
RBP_initial_data = RBP_data_scrap((upstream_exon+intron_seq+downstream_exon))
RBP_data = sorted(RBP_initial_data,key=lambda x:x[1]) # Sort the RBP data list based on position value, which is in 2nd columm
RBP_time2 = timer()
print("The RBP data scrapping takes ", int(RBP_time2-RBP_time1), "second(s) to finish. ")


# dissociation constant data for RBPs
kd_data_list = []
print("\n")
print("Extract RBP binding affinity data of crRNA from the csv file in progress:")
with open('RBP_binding_affinity_data.csv',"r") as file:
    filereader = csv.reader(file)
    for row in tqdm(filereader):
        kd_data_list.append(row)

kd_data_list[0][0] = kd_data_list[0][0][-4:]


RBP_competition_score_list = []
print("\n")
print("RBP-score calculation in progress:")
for each_gRNA in tqdm(gRNA_seq_list):
    temp_score = RBP_competition_score(gRNA_start_site,each_gRNA, gRNA_seq_list, RBP_data,kd_data_list)
    RBP_competition_score_list.append(temp_score)

# Final_score_list for RBP competition: variable name: RBP_competition_score_list

# ------------------------------Separation Line -----------------------------



# ---------------------------------------------------------------------------



# ------------------------------Separation Line -----------------------------
# pre-structure of crRNA analysis
"""
pre_structure_data_list =[]
print ("\n")
print ("Data scraping from Nupack for pre-crRNA structure in progress:")
temp_driver = webdriver.Chrome()
for gRNA in tqdm(gRNA_seq_list):
    gRNA_seq = gRNA[-gRNA_length:]
    pre_structure = direct_repeat_sequence + gRNA_seq + direct_repeat_sequence
    pre_structure_data = Nupack_data_scrap(pre_structure,temp_driver)
    pre_structure_data_list.append(pre_structure_data)
temp_driver.quit()

with open('Pre_crRNA_structure_Nupack_data.csv','w',newline='') as fp:
    a = csv.writer(fp,delimiter=',')
    a.writerows(pre_structure_data_list)
"""
pre_crRNA_structure_data_list = []
with open("Pre_crRNA_structure_Nupack_data.csv", "r") as nfile:
    nreader = csv.reader(nfile)
    for row in tqdm(nreader):
        pre_crRNA_structure_data_list.append(row)
for each_gRNA in pre_crRNA_structure_data_list:
    for data in each_gRNA:
        each_gRNA[each_gRNA.index(data)] = ast.literal_eval(data)
for each_gRNA in pre_crRNA_structure_data_list:
    for data in each_gRNA:
        for num in data:
            data[data.index(num)] = float(num)

pre_gRNA_start_pos = len(direct_repeat_sequence)+1
pre_gRNA_end_pos = pre_gRNA_start_pos + gRNA_length - 1

calculation_list = []
for each_gRNA in pre_crRNA_structure_data_list:
    temp_list =[]
    for data in each_gRNA:
        if(data[0]>=pre_gRNA_start_pos and data[0]<=pre_gRNA_end_pos and data[1]==-1):
            temp_list.append(data[2])
    diff = gRNA_length - len(temp_list)
    if(diff>0):
        for x in range(diff):
            temp_list.append(0.001)
    calculation_list.append(temp_list)

pre_crRNA_structure_score_list = []
print("\n")
print("The pre-crRNA secondary structure score calculation in progress:")
for each_gRNA in tqdm(calculation_list):
    temp_score = 1
    for prob in each_gRNA:
        temp_score *= prob
    #temp_score *= pre_crRNA_weight
    pre_crRNA_structure_score_list.append(temp_score)

# ------------------------------Separation Line -----------------------------



# ---------------------------------------------------------------------------



# ------------------------------Separation Line -----------------------------
# GC content analysis:
GC_content_score_list = []
print("\n")
print("Analysis of GC content is in progress:")
for gRNA in tqdm(gRNA_seq_list):
    if GC_content(gRNA[-gRNA_length:]) >= GC_threshold_low and GC_content(gRNA[-gRNA_length:]) <= GC_threshold_high:
        GC_content_score_list.append(0)
    else:
        GC_content_score_list.append(GC_content_penalty_score)
# Final Score list for GC content, variable name: GC_content_score_list

# ------------------------------Separation Line -----------------------------



# ---------------------------------------------------------------------------



# ------------------------------Separation Line -----------------------------
# Off target searching begins

#file = open("human-cDNA.txt","r")
#cDNA_seq = file.readline()

cDNA_data_list = []
with open("human-cDNA.csv", "r") as nfile:
    nreader = csv.reader(nfile)
    for row in tqdm(nreader):
        cDNA_data_list.append(row)

off_target_data_output = []

for gRNA in tqdm(gRNA_seq_list):
    num_mismatch, mismatch_list = off_target_mismatch(cDNA_data_list,gRNA)
    off_target_gRNA = [num_mismatch, mismatch_list]
    off_target_data_output.append(off_target_gRNA)

with open('Off_target_data.csv','w',newline='') as fp:
    a = csv.writer(fp,delimiter=',')
    a.writerows(off_target_data_output)

off_target_data_list = []
with open("Off_target_data.csv", "r") as nfile:
    nreader = csv.reader(nfile)
    for row in tqdm(nreader):
        off_target_data_list.append(row)

for each_gRNA in off_target_data_list:
    for data in each_gRNA:
        each_gRNA[each_gRNA.index(data)] = ast.literal_eval(data)

off_target_score_list = []
print("\n")
print("Off target score calculation in progress:")
for each_gRNA in tqdm(off_target_data_list):
    if(each_gRNA[0]>100):
        off_target_score_list.append(off_target_overwhelm)
    elif(each_gRNA[0]==0):
        off_target_score_list.append(0)
    else:
        for num in each_gRNA[1]:
            temp_score = 0
            if(num==5):
                temp_score += mm5_score
            elif(num==4):
                temp_score += mm4_score
            elif(num==3):
                temp_score += mm3_score
            elif(num==2):
                temp_score += mm2_score
            elif(num==1):
                temp_score += mm1_score
            elif(num==0):
                temp_score += mm0_score
            else:
                temp_score += default_mm_score
        off_target_score_list.append(temp_score)

# Final score list for off-target binding: variable name: off_target_score_list
# ------------------------------Separation Line -----------------------------



# ---------------------------------------------------------------------------



# ------------------------------Separation Line -----------------------------

# Final overall score calculation:
# Score lists of different variables:
# ---> weighted score for gRNA's secondary structure - variable name: Nupack_gRNA_final_score
# ---> weighted score for RBP competition            - variable name: RBP_competition_score_list
# ---> penalty score for GC content                  - variable name: GC_content_score_list
# ---> off-target binding score                      - variable name: off_target_score_list
# ---> score for pre-crRNA strucure                  - variable name: pre_crRNA_structure_score_list


bool_list = []
index_list =[]
print ("Final filter of the gRNAs in process: ")
for n in tqdm(range(len(gRNA_seq_list))):
    if (GC_content_score_list[n] <= cutoff_GC_content and off_target_score_list[n] <= cutoff_off_target and RBP_competition_score_list[n] <= cutoff_RBP and Nupack_gRNA_final_score[n] >= cutoff_gRNA and pre_crRNA_structure_score_list[n] >= cutoff_pre_crRNA):
        bool_list.append(True)
        index_list.append(n)
    else:
        bool_list.append(False)

for index in index_list:
    print("\n")
    print("Secondary structure score:  ",Nupack_gRNA_final_score[index])
    print("Pre-crRNA secondary structure score:  ",pre_crRNA_structure_score_list[index])
    print("RBP intereference score:  ", RBP_competition_score_list[index])
    print("GC Content penalty score:  ",GC_content_score_list[index])
    print("Off target penalty score:  ",off_target_score_list[index])

# Log recording ends
if(log_judge):
    sys.stdout = old_stdout
    log_file.close()
