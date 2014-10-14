import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#this command prints out a list of genome assession number (from full genome) with taxonomy domain
#usage: for i in *.gbk; do python ~/Documents/Projects/KBase/eco-R/genbank-fan/extract_dbsource_from_gbk.py $i; done > hit_id_accession.txt 

for record in list(SeqIO.parse(sys.argv[1], 'genbank')):
    #print record
    tax = record.annotations["taxonomy"][1]
    id = record.id
    org = record.annotations["source"]
    print id + '\t' + tax 
