##input: /Users/metagenomics/Documents/Databases/uniprot_tremble.dat or uniprot_sprot.dat

import sys
import os
from Bio import SeqIO
#import gzip

#This script uses biopython to get taxonomy from uniprot .dat file
'''
record.annotations         record.letter_annotations
record.dbxrefs             record.lower
record.description         record.name
record.features            record.reverse_complement
record.format              record.seq
record.id                  record.upper
'''

def get_taxa(uniprot_dat):
	taxa_to_print=[]
	for record in SeqIO.parse(uniprot_dat, "swiss"):
#		taxa_to_print.append(record.id)
		taxa_to_print.append(uniprot_dat.split(".")[0])
		taxa_to_print.append(record.annotations['organism'])
		for taxa in record.annotations['taxonomy']:
			taxa_to_print.append(taxa)
	return '\t'.join(taxa_to_print)

uniprot_dat = sys.argv[1:]

for f in uniprot_dat:
	taxa = get_taxa(f)
	print(taxa)
