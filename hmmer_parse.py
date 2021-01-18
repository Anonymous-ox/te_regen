'''
Input: query result (hmmer3-tab in folder E:\HMMER_output\)
Output: visualisation of query result (parsing)
'''
import os
import pandas

def parsing(filename):
    with open(filename) as handle:      #open and obtain contents from the result files
        content = handle.readlines()

    parse_target = []       #parse the results into a list
    for i in range(0, len(content)):
        temp = content[i]
        if temp[0] != '#':
            parse_target.append(temp[:-1])

    filelist = []       #arrange elements into list of lists - for pandas dataframe conversion and export
    for i in parse_target:      
        temp = i.partition('Danio')
        splitnum = str(temp[0]).split(" ")
        templist = []
        for j in splitnum:
            if j != '':
                templist.append(j)
        descr = temp[1] + temp[2]
        templist.append(descr)
        filelist.append(templist)
    return filelist

def main():
    #obtain necessary elements for filename iteration
    genelist = pandas.read_excel(r'F:\Biology\03 Grant_Proposal\10 Mini-project\Regen_rel_genes.xlsx')
    list_genename = genelist['Gene'].to_list()
    list_chrom = genelist['Genomic_coordinates'].to_list()
    listlen = int(len(list_genename))
    chrom = []
    for i in list_chrom:
        temp = i.partition(':')
        chrom.append(temp[0])

    path = r"E:\\HMMER_output\\"
    os.chdir(path)
    grandlist = []

    #export the dataframe into a *.csv file
    for i in range(0, listlen):    
        filename = "D_rerio_seqfrag_" + list_genename[i] + "_" + chrom[i] + "_output"
        filelist = parsing(filename)
        grandlist.extend(filelist)
    
    df = pandas.DataFrame(grandlist, columns = ['target name', 'target accession', 'query name', 'query accession', 'query start pos', 'query end pos', 'target seq start pos', 'target seq end pos', 'envfrom', 'envto', 'target seq length', 'strand', 'E-value', 'bit score', 'bias', 'description']) #for detailed descriptions, see the HMMER user guide at http://eddylab.org/software/hmmer3/3.1b2/Userguide.pdf on pages 69 and 70
    df.to_csv("D_rerio_Results.csv", index = False)

if __name__ == "__main__":
    main()