## input file: anything resembles /Users/metagenomics/Documents/Fan/scratch/xander_701/Asp/nucl_cdhit.fasta.clstr

import sys
import os
import re
from itertools import groupby

def clstr_iter(cdhit_clstr):
	f = open(cdhit_clstr)
	citer = (x[1] for x in groupby(f, lambda line: line[0] == ">"))
	for cluster in citer:
		l = []
		for line in next(citer):
#			if line.startswith("0"):
			if "*" in line:
				string = re.split("\t| |>|\.|\||;", line)
				cluster = string[3]
			else: 
				string = re.split("\t| |>|\.", line)
				sample_seq = string[3]
				l.append(sample_seq)
		yield cluster, l 

clstr = sys.argv[1]
d = dict(clstr_iter(clstr))
for item in d:
	for ss in d[item]:
		print("%s\t%s" % (item, ss))

