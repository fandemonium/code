#!/usr/bin/python
# to use: navigate to pfam_hmm_done/ana/ folder, do: for i in *; do python ~/Documents/Fan/scratch/code/cdhit_clst_parser.py /Users/metagenomics/Documents/Fan/scratch/xander_701/$i/nucl_cdhit.fasta.clstr > /Users/metagenomics/Documents/Fan/scratch/blast_desc/clstr_parsed/$i.x701.clstr.parsed; done#

## input file: anything resembles /Users/metagenomics/Documents/Fan/scratch/xander_701/Asp/nucl_cdhit.fasta.clstr

import sys
import os
from collections import Counter
import re

f = open(sys.argv[1], 'rU')
#output = open(sys.argv[2], 'w')

for n, line in enumerate(f):
	line = line.rstrip()
	j = n+1
	if line.startswith(">Cluster"):
		i = n
		string = re.split("\n", line)
		id = string[0]
		#print i, id
	if line.endswith("*"):
		lexeme = re.split("\t| |>|\...", line)
		contig = lexeme[3]
		#print n, line
		#output.write('%s\t%s\t%s\n' % (i, id, contig))
		print '%s\t%s\t%s' % (i, id, contig)
print j
