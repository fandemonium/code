##input: /Users/metagenomics/Documents/Databases/uniprot_tremble.dat or uniprot_sprot.dat

import sys
import os
from Bio import SeqIO

uniprot = open(sys.argv[1], "rU")

for record in SeqIO.parse(uniprot, "swiss"):
	id = record.id
	taxa = record.annotations['taxonomy']
	#if record.annotations['taxonomy'] >1:
	#	domain = record.annotations['taxonomy'][1]
	#	if kingdom != 'Eukaryota':
	#		print "%s\t%s" % (id, kingdom)
	#	else:
	#		if domain == 'Fungi':
	print "%s\t%s" % (id, taxa)
