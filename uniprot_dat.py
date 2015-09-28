##input: /Users/metagenomics/Documents/Databases/uniprot_tremble.dat or uniprot_sprot.dat

import sys
import os
from Bio import SeqIO
#import gzip

uniprot = open(sys.argv[1], "rU")

taxa_to_print=[]
for record in SeqIO.parse(uniprot, "swiss"):
#	print record
#	id = record.id
	taxa_to_print.append(sys.argv[1].split(".")[0])
	taxa_to_print.append(record.annotations['organism'])
	for taxa in record.annotations['taxonomy']:
		taxa_to_print.append(taxa)
print '\t'.join(taxa_to_print)
	#if record.annotations['taxonomy'] >1:
	#	domain = record.annotations['taxonomy'][1]
	#	if kingdom != 'Eukaryota':
	#		print "%s\t%s" % (id, kingdom)
	#	else:
	#		if domain == 'Fungi':
#	print '\t'.joint(strain, taxa_to_print)
