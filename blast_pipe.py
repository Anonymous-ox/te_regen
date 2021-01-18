'''
Input: pre-downloaded genome database (*.fna) from NCBI genome/assembly website
Input: excel (*.xlsx) file that documents genes and genomic coordinates of interest (sample included)
Prerequisite: NCBI-BLAST installed locally and genomic database constructed
Output: fasta (*.fasta) file that includes 500 thousand basepairs upstream and downstream of target gene, located in the database using genomic coordinates
'''
import pandas as pd 
import sys
import os
import subprocess

def get_coordinate (coor): #obtain coordinates as int and chromosome numbers without punctuations
    csplit = coor.split()
    chrom, start, end = csplit[0], csplit[1], csplit[3]
    chrom = chrom.split(':')[0]
    chromnum = int(chrom[3:])
    l = len(start.split(','))
    starta, enda = '', ''
    for a in range(0, l): 
        enda += end.split(',')[a]
        starta += start.split(',')[a]
    return chromnum, starta, enda

def generate_database(genname, chromnum, start, end):
    os.chdir(r"E:\NCBI\blast-2.11.0+\db") #set working directory
    path = os.getcwd()
    path = path + "\\Drerio_Chr" + str(chromnum)
    #path = path + "\\" + species_name  #to be added when there are multiple species
    while True:
        try:
            os.mkdir(path)
            break
        except FileExistsError:
            break
    os.chdir(path)  #create a chromosome specific folder and set path to that folder   
    start = int(start) - 500000
    end = int(end) + 500000      #number of bps to take upstream and downstream the target gene (1 million in total, in this instance)
    entrynum = chromnum + 11 
    entry = "NC_0071" + str(entrynum) + ".7"    #generate accession entry number
    name = 'D_rerio_seqfrag_' + genname + '_Chr' + str(chromnum)
    subprocess.run("blastdbcmd -db daniorerio1 -entry {} -range {}-{} > {}.fasta".format(entry, str(start), str(end), name), shell = True)

def main():
    #Input: genes with genomic coordinates, as well as all the homologues known. Example file downloadable from GitHub.
    df = pd.read_excel(r'F:\Biology\03 Grant_Proposal\10 Mini-project\Regen_rel_genes.xlsx')

    list_gen_coor = df['Genomic_coordinates'].to_list() #assign genomic coordinates to a list
    list_gen_name = df['Gene'].to_list()    #assign gene names to a list
    #list_species_name = df['Species'].to_list() #assign species names

    for i in range(0, len(list_gen_coor)): #iteration of obtaining coordinates & creating folders + fasta files
        coor = list_gen_coor[i]
        genname = list_gen_name[i]
        #spename = list_species_name[i]
        chrom, start, end = get_coordinate(coor)
        generate_database(genname, chrom, start, end)
        #generate_database(spename, genname, chrom, start, end)

if __name__ == "__main__":
    main()

#biopython genbank metadata
#os make directory and change directory