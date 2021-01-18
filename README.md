# te_regen
Repository for project proposal 'Comparative study of the potential role of transposable elements in vertebrate regeneration'
How to use the pipeline:

Pipeline working instructions
1.	Install command line BLAST and set up a D. rerio database as per instructions from https://www.ncbi.nlm.nih.gov/books/NBK52637/.
2.	Prepare the target gene file with genomic coordinates (example file available from GitHub Repository).
3.	Run blast_pipe.py. Note that the script does not automatically generate the parent directory* so these have to be changed accordingly.
4.	blast_pipe.py isolates genomic regions upstream and downstream of genes in the input * .xlsx file and automatically generate folders to group the genomic regions from the same chromosome.
5.	Store a replicate of all the search results in a single folder in a portable storage device before shifting to a Linux operating system.
6.	On the Linux operating system, store these results in the hmmer folder defined by path in line 20 of hmmer_pipe.py.
7.	Download TE reference sequences (both * .hmm and * .sto files) from the Dfam online database and store them into the same folder as defined in step 6. We used https://www.dfam.org/family/DF0001345/summary and https://www.dfam.org/family/DF0001344/summary as working examples.
8.	Run hmmer_pipe.py on the Linux operating system. It will search for putative TE sequences within the genomic regions specified in the BLAST search result files. It will export some search files in the path specified in line 16.
9.	Store these search results to a portable storage device and shift back to a Windows operating system.
10.	On the Windows operating system, ensure the search results are stored in the path specified in line 42 of the hmmer_parse.py file. 
11.	Run hmmer_parse.py, which will generate a * .csv parsed output file in the same directory with the name of D_rerio_results.csv. This will be the search result in a format compatible for further research.

* The parent directories appear in lines 25, 45 of blast_pipe.py, lines 13, 16, 20, 34 of hmmer_pipe.py, and lines 33, 42 of hmmer_parse.py.
