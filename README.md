![9ec81688-4d89-40c1-b547-5c9810963752](https://user-images.githubusercontent.com/29665985/27970945-d206ef36-631e-11e7-97a0-36deb037e9af.png)
# SpliceMIT - Splice Modelling (Intronic) Technology
### SpliceMIT is a tool to analyze and produce the most effective gRNA sequences in a RNA splicing setting.<br />
### example RBPs: dCas13a, MS2, L7Ae, RCas9 <br />
### Language: Python <br />
### Package required: Selenium, urllib, bs4(beautiful soup), tqdm <br />
<br />

#### *File explanation*: <br />
1.	Nupack_data.csv : <br />sample data for secondary structure of the crRNA. The results are obtained from Nupack developed by Caltech.
2.	Off_target_data.csv: <br />sample data for off-target in a human cell (analyze using the homo sapiens cDNA sequence)
3.	Pre_crRNA_structure_Nupack_data.csv: <br />sample data for secondary structure of the pre-crRNA, also obtained from Nupack.
4.	RNA_binding_affinity_data.csv: <br />containing the dissociation constant for over 90 RNA binding proteins found in Human and Drosophila. (THIS IS NOT A SAMPLE FILE)
5.	human-cDNA-part1.rar & human-cDNA-part2: <br />compressed text file of human cDNA sequence. The size is approximately 300 million bases. The original FASTA file is from the UCSC genome browser.<br />
<br />   

#### *How to use SpliceMIT*:<br />
1.	Download model.py and RNA_binding_affinity_data.csv (same directory)<br />
2.	Open model.py and read all annotations before running.<br />
3.	Modify the variables in the “Global Constant” region. It should be right below all the functions<br />
4.	Run the program and wait for the result. (The sample running is on a 850nt intron – 708 gRNAs, and took approximately 36 hours in total)<br />
5.	You will see the top 10 crRNA sequences<br />
<br />

#### *Variables you PROBABLY want to change*:<br />
1.	gRNA_length <br />
2.	tracrRNA_seq <br />
3.	upstream_exon <br />
4.	downstream_exon <br />
5.	direct_repeat_sequence <br />
6.	(All weight values) <br />


<br />
<br />

### Citations: <br />

#### GC content: <br />
>  1.Tessa G. Montague, José M. Cruz, James A. Gagnon, George M. Church, Eivind Valen; CHOPCHOP: a CRISPR/Cas9 and TALEN web tool for genome editing. Nucleic Acids Res 2014; 42 (W1): W401-W407. doi: 10.1093/nar/gku410 <br />
>  2.Wang, Tim et al. “Genetic Screens in Human Cells Using the CRISPR/Cas9 System.” Science (New York, N.Y.) 343.6166 (2014): 80–84. PMC. Web. 5 July 2017. <br />
>  3.Tsai, Shengdar Q. et al. “GUIDE-Seq Enables Genome-Wide Profiling of off-Target Cleavage by CRISPR-Cas Nucleases.” Nature biotechnology 33.2 (2015): 187–197. PMC. Web. 5 July 2017. <br />
<br />

#### RBPmap: <br />
>  1.Inbal Paz, Idit Kosti, Manuel Ares, Jr, Melissa Cline, Yael Mandel-Gutfreund; RBPmap: a web server for mapping binding sites of RNA-binding proteins. Nucleic Acids Res 2014; 42 (W1): W361-W367. doi: 10.1093/nar/gku406 <br />
<br />

#### Nupack: <br />
>  1.J. N. Zadeh, C. D. Steenberg, J. S. Bois, B. R. Wolfe, M. B. Pierce, A. R. Khan, R. M. Dirks, N. A. Pierce. NUPACK: analysis and design of nucleic acid systems. J Comput Chem, 32:170–173, 2011. <br /> 
<br />

#### RNA binding affinity:<br />
>Citations are included in the file: RNA_binding_affinity_data.csv <br />
