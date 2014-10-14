#!/usr/bin/python
##?? early version of count_clst_abundance.py ??##


import sys
import os
from collections import Counter
import re

#if len(sys.argv) != 4:
#	print "USAGE: cdhit_clst_parser.py <pattern> <cdhit.clstr> <out_file>"
#	sys.exit(1)

j =0

f = open(sys.argv[1], 'rU')
#output = open(sys.argv[2], 'w')

for n, line in enumerate(f):
	line = line.rstrip()
	if line.startswith(">Cluster"):
		string = re.split("\n", line)
		id = string[0]
		if j == 0:
			print id;
		else:
			print"contig_count=",j
			print id;
	if line.endswith("*"):
		lexeme = re.split("\t| |>|\...", line)
		contig = lexeme[3]
		print line
		j = 1
		#output.write('%s\t%s\t%s\n' % (i, id, contig))
		#print '%s\t%s\t%s' % (j, id, contig)
	else:
		j = j+1
print "contig_count=",j
