'''
Input: *.fasta database from last step (step 1). 
Input: *.hmm and *.sto files as transposable element reference sequences with this analysis, downloaded from the Dfam database.
Output: query result files in hmmer3-tab format
Runs on Linux system
'''
import subprocess
import sys
import os, os.path

def export_tblout (te_name, db_name):   ##run command line to store search output into hmmer3-tab files in the tutorial folder
    output_name = db_name[:-6] + '_output'  #strip '.fasta' from the file name
    subprocess.run("cd /home/yy/hmmer-3.3.1/tutorial/", shell = True)
    subprocess.run("hmmbuild {}.hmm {}.stk".format(te_name, te_name), shell = True)
    #subprocess.run("nhmmer --tblout /home/yy/hmmer-3.3.1/tutorial/{} {}.hmm {}".format(output_name, te_name, db_name), shell = True) #make hmm table to target directory
    subprocess.run("nhmmer --tblout /media/yy/Backup_Plus/HMMER_output/{} {}.hmm {}".format(output_name, te_name, db_name), shell = True)
    #subprocess.run("nhmmer {}.hmm {} > {}".format(te_name, db_name, output_name), shell = True) #make hmm file

def number_of_dbs ():   #returns the number of databases and their names in the directory
    path = '/home/yy/hmmer-3.3.1/tutorial/'
    list = os.listdir(path)
    newlist = []
    length = 0
    for element in list:
        jdstr = element[:15]
        if jdstr == 'D_rerio_seqfrag':
            length += 1
            newlist.append(element)
        else:
            length = length
    return(length, newlist)

def main():  
    path = '/home/yy/hmmer-3.3.1/tutorial/'
    os.chdir(path) #fasta databases have been stored in this directoryte_name = 'dr_ex1'
    number, newlist = number_of_dbs()    #number of databases in the directory
    te_name = 'dr_ex1'  #name of the TE reference sequence in the directory
    
    for i in range(0, number):  #search query sequence against all the databases
        db_name = newlist[i]
        export_tblout(te_name, db_name) #export hmmer3-tab format query result

if __name__ == "__main__":
    main()