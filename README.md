![9ec81688-4d89-40c1-b547-5c9810963752](https://user-images.githubusercontent.com/29665985/27970945-d206ef36-631e-11e7-97a0-36deb037e9af.png)
# SpliceMIT - Splice Modelling (Intronic) Technology
>### SpliceMIT is a tool to analyze and produce the most effective gRNA sequences in an RNA splicing setting.<br />
>### example RBPs: dCas13a, MS2, L7Ae, RCas9 <br />
>### Language: Python <br />
>### Package required: Selenium, tqdm <br />
<br />

### **Read below and ALL ANNOTATIONS in model.py before running!!!**

#### *File explanation*: <br />
>1.	Nupack_data.csv : <br />sample data for secondary structure of the crRNA. The results are obtained from Nupack developed by Caltech.
>2.	Off_target_data.csv: <br />sample data for off-target in a human cell (analyze using the homo sapiens cDNA sequence)
>3.	Pre_crRNA_structure_Nupack_data.csv: <br />sample data for secondary structure of the pre-crRNA, also obtained from Nupack.
>4.	RNA_binding_affinity_data.csv: <br />containing the dissociation constant for over 90 RNA binding proteins found in Human and Drosophila. (THIS IS NOT A SAMPLE FILE)
>5.	human-cDNA-part1.rar & human-cDNA-part2: <br />compressed text file of human cDNA sequence. The size is approximately 300 million bases. The original FASTA file is from the UCSC genome browser.<br />
<br />   

#### *How to use SpliceMIT*:<br />
>1.	Download model.py and RNA_binding_affinity_data.csv (same directory)<br />
>2.	Open model.py and **read ALL annotations** before running.<br />
>3.	Modify the variables in the “Global Constant” region. It should be right below all the functions<br />
>4.	Run the program and wait for the result. (The sample running is on a 850nt intron – 708 gRNAs, and took approximately 36 hours in total)<br />
>5.	You will see the top 10 crRNA sequences<br />
>6. You may want to use PhantomSJ as a virtual webdriver application if you are running the program directly on your work computer/laptop. Please go check out http://phantomjs.org/ <br />
<br />

#### *Variables you PROBABLY want to change*:<br />
>1.	gRNA_length <br />
>2.	tracrRNA_seq <br />
>3.	upstream_exon <br />
>4.	downstream_exon <br />
>5.	direct_repeat_sequence <br />
>6.	(All weight values) <br />
<br />

#### *Factors that taken into account:* <br />
> 1. Off-target binding of gRNA <br />
> 2. GC content of the crRNA sequence <br />
> 3. Secondary structure of the crRNA structure <br />
> 4. Secondary structure of the pre-gRNA structure <br />
> 5. Competition of different RNA-binding proteins at the site <br />
> 6. Location of ISE and ISS of the given intron is not included but could be easily implemented by adding a list and apply bonus/penalty scores. <br />
<br />

#### *RBP Interference Score Algorithm:*
>![codecogseqn 14](https://user-images.githubusercontent.com/29665985/27987285-1667b48e-63d9-11e7-9d3b-7e37eabf201a.gif) <br />
>![codecogseqn 3](https://user-images.githubusercontent.com/29665985/27973208-3d452120-6327-11e7-825c-c63ecd6dc7d7.gif) <br />
>![codecogseqn 4](https://user-images.githubusercontent.com/29665985/27973317-a481661e-6327-11e7-81e4-85f5d02110d5.gif) <br />
> a is the weight value; <br />
> k is the weight-power constant; <br /> 
> Kd is the dissociation constant for the RBP;<br /> 
> Lb is the length of binding; <br />
> Lm is the length of RBP-binding motif; <br />
> [RBP] is the concentration of an RNA-binding protein(set to default) <br />
<br />

#### *For Secondary Structure Probability Score*:
>![codecogseqn 12](https://user-images.githubusercontent.com/29665985/27980540-bc5257aa-634d-11e7-94c9-21684a58b5c2.gif) <br />
> Pn is the probability of not having stem-loop or hairpin structure for a crRNA sequence <br />
> Pn-base is the probability of a base not binding to any other bases on the crRNA <br />
<br />

#### *crRNA Secondary Structure Score Algorithm:*
>![codecogseqn 5](https://user-images.githubusercontent.com/29665985/27974015-22e0a7f2-632a-11e7-87c1-024d5cd66d6d.gif) <br />
>![codecogseqn 6](https://user-images.githubusercontent.com/29665985/27974172-d6fd853e-632a-11e7-9f94-3589de98c04e.gif) <br />
>![codecogseqn 7](https://user-images.githubusercontent.com/29665985/27974339-96679c8e-632b-11e7-8ed9-605a06209def.gif) <br />
> P is the weighted probability score <br />
> Kw is the weight power <br />
> P-target is the target maximum probability score <br />
> P-n-max is the maximum value of all unweighted proabilities <br />
<br />

#### *Pre-gRNA Secondary Structure Score Algorithm:*
>![codecogseqn 8](https://user-images.githubusercontent.com/29665985/27974631-d52888b0-632c-11e7-8451-7e7b6113c25e.gif) <br />
>![codecogseqn 9](https://user-images.githubusercontent.com/29665985/27974680-02468284-632d-11e7-9d94-8143f5e1edf3.gif) <br />
>![codecogseqn 10](https://user-images.githubusercontent.com/29665985/27974788-797d4fa4-632d-11e7-8675-2064888dd0f0.gif) <br />
>![codecogseqn 11](https://user-images.githubusercontent.com/29665985/27974867-cd033328-632d-11e7-88f2-4202404c9285.gif) <br />
> P is the weighted probability score <br />
> c is the root limitation factor constant <br />
> m-p is the pre-set root constant <br />
<br />




<br />
<br />

### Citations: <br />

#### GC content: <br />
>  Tessa G. Montague, José M. Cruz, James A. Gagnon, George M. Church, Eivind Valen; CHOPCHOP: a CRISPR/Cas9 and TALEN web tool for genome editing. Nucleic Acids Res 2014; 42 (W1): W401-W407. doi: 10.1093/nar/gku410 <br />
>  Wang, Tim et al. “Genetic Screens in Human Cells Using the CRISPR/Cas9 System.” Science (New York, N.Y.) 343.6166 (2014): 80–84. PMC. Web. 5 July 2017. <br />
>  Tsai, Shengdar Q. et al. “GUIDE-Seq Enables Genome-Wide Profiling of off-Target Cleavage by CRISPR-Cas Nucleases.” Nature biotechnology 33.2 (2015): 187–197. PMC. Web. 5 July 2017. <br />
<br />

#### RBPmap: <br />
>  Inbal Paz, Idit Kosti, Manuel Ares, Jr, Melissa Cline, Yael Mandel-Gutfreund; RBPmap: a web server for mapping binding sites of RNA-binding proteins. Nucleic Acids Res 2014; 42 (W1): W361-W367. doi: 10.1093/nar/gku406 <br />
<br />

#### Nupack: <br />
>  J. N. Zadeh, C. D. Steenberg, J. S. Bois, B. R. Wolfe, M. B. Pierce, A. R. Khan, R. M. Dirks, N. A. Pierce. NUPACK: analysis and design of nucleic acid systems. J Comput Chem, 32:170–173, 2011. <br /> 
<br />

#### RNA binding affinity:<br />
>Citations are included in the file: RNA_binding_affinity_data.csv <br />

<br />
Codes and algorithms by: Qianchang Dennis Wang <br />
Cooperated with: Ben Kaplan 19', Molly Stephens 18', Adil Yusuf 20' <br />
Also speical thanks to MIT Burge Lab and Harvard ChopChop developers.
