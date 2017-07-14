![9ec81688-4d89-40c1-b547-5c9810963752](https://user-images.githubusercontent.com/29665985/27970945-d206ef36-631e-11e7-97a0-36deb037e9af.png)
# SpliceMIT 2.0 - Splice Modelling (Intronic) Technology 2.0
>### SpliceMIT is a tool to analyze and produce the most effective gRNA sequences in an RNA splicing setting based on user inputs of an intron sequence, upstream and downstream 20 nt sequence, gRNA size, and tracrRNA sequence. It sets up cut-off values to filter the gRNAs and eventually provide a list of effective gRNA sequences. <br />
>### example RBPs: dCas13a, MS2, L7Ae, RCas9 <br />
>### Language: Python <br />
>### Package required: Selenium, tqdm <br />
<br />

### **Read below and ALL ANNOTATIONS in model.py before running!!!**

#### *File explanation*: <br />
>1.	Nupack_data.csv : <br />sample data for secondary structure of the crRNA. The results are obtained from Nupack developed by Caltech.
>2.	Off_target_data.csv: <br />sample data for off-target in a human cell (analyze using the homo sapiens cDNA sequence)
>3.	Pre_crRNA_structure_Nupack_data.csv: <br />sample data for secondary structure of the pre-crRNA, also obtained from Nupack.
>4.	RNA_binding_affinity_data.csv: <br />containing the dissociation constant for over 90 RNA binding proteins found in Human and Mouse. (THIS IS NOT A SAMPLE FILE)
>5.	human-part1.rar & human-part2: <br />compressed FASTA file of human cDNA sequence(txt format). The size is approximately 300 million bases. The original FASTA file is from the UCSC genome browser.<br />
<br />   

#### *How to use SpliceMIT*:<br />
>1.	Download model.py; FASTA.py; RNA_binding_affinity_data.csv and both human-part1.txt.rar and human-part2.txt.rar (in the same directory)<br />
>2. Unzip the rar files and combine them into one single txt file. Name it as "human.txt" <br />
>3. Run the FASTA.py in order to transfer fasta format into simple "ATCG". <br />
>4.	Open model.py and **read ALL annotations** before running.<br />
>5.	Modify the variables in the “Global Constant” region. It should be right below all the functions<br />
>6.	Run the program and wait for the result. (The sample running is on a 850nt intron – 708 gRNAs, and took approximately 36 hours in total)<br />
>7.	You will see the top 10 crRNA sequences<br />
>8. You may want to use PhantomJS as a virtual webdriver application if you are running the program directly on your work computer/laptop. Please go check out http://phantomjs.org/ <br />
<br />

#### *Variables you PROBABLY want to change*:<br />
>1.	tracrRNA_seq <br />
>2.	direct_repeat_sequence <br />
>3.	(All weight values) <br />
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
>![codecogseqn 15](https://user-images.githubusercontent.com/29665985/28218617-13607872-6887-11e7-9f07-7f06e11b66c5.gif)<br />
>![codecogseqn 3](https://user-images.githubusercontent.com/29665985/27973208-3d452120-6327-11e7-825c-c63ecd6dc7d7.gif) <br />
> a is the weight value; <br />
> Kd is the dissociation constant for the RBP;<br /> 
> Lb is the length of binding; <br />
> Lm is the length of RBP-binding motif; <br />
> [RBP] is the concentration of an RNA-binding protein(set to default) <br />
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
Cooperated with: Ben Kaplan 19', Molly Stephens 18', Adil Yusuf 20', Ronit Langer 20', and our amazing leader - Brian Teague <br />
Also speical thanks to MIT Burge Lab, Harvard Schier Lab and Valen Lab at University of Bergen.
