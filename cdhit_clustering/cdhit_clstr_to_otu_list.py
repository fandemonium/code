## input file: anything resembles /Users/metagenomics/Documents/Fan/scratch/xander_701/Asp/nucl_cdhit.fasta.clstr

import sys
import os
import re
from itertools import groupby

def clstr_iter(cdhit_clstr):
	f = open(cdhit_clstr)
	citer = (x[1] for x in groupby(f, lambda line: line[0] == ">"))
	for header in citer:
		header = header.next()[1:].strip().split(" ")
		header = "OTU_" + header[1]
		seq = {}
		for line in citer.next():
			string = re.split("\t| |>|\.", line)
			new_id = string[3]
			if  new_id not in seq:
				seq[new_id] = [new_id]
			else:
				seq[new_id].append(new_id)
		yield header, seq

clstr = sys.argv[1]
d = dict(clstr_iter(clstr))
for item in d:
	for s in d[item]:
		print "%s\t%s" % (item, s)

