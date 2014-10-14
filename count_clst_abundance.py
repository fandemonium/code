#!/usr/bin/python
## does exactly what cdhit_clst_parser.py and clst_abundance.py together do. 

import sys
import os
from collections import Counter
import re

## for i in *; do python ~/Documents/Fan/scratch/code/count_clst_abundance.py ~/Documents/Fan/scratch/xander_702/$i/nucl_cdhit.fasta.clstr > ~/Documents/Fan/scratch/parsed_files/clstr_parsed/x702_"$i".clstr.parsed; done

j =0

f = open(sys.argv[1], 'rU')

for line in f:
	line = line.rstrip()
	if line.startswith(">Cluster"):
		string = re.split("\n", line)
		id = string[0]
		if j == 0:
			print '%s\t' % (id),
		else:
		# print contig name followed by the total number j	
			print '%s\t%s\n%s\t' % (contig,j,id),

	if line.endswith("*"):
		lexeme = re.split("\t| |>|\...", line)
		contig = lexeme[3]
		#print contig + '\t'
		j = 1

	else:
		j = j+1
# print last line 
print '%s\t%s' % (contig,j)
