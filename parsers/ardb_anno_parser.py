## input file: anything resembles /Users/metagenomics/Documents/Fan/scratch/xander_701/Asp/nucl_cdhit.fasta.clstr

import sys
import os
import re
from itertools import groupby

l = []
for n, lines in enumerate(open(sys.argv[1], 'rU')):
	if n == 0:
		continue
	else:
		line = lines.strip().split("\t")
		mock_id = line[0]
		l.append(mock_id)

with open(sys.argv[2]) as anno:
	d = {}
	groups = (x[1] for x in groupby(anno, lambda line: line[0] == ">"))
#	groups = groupby(anno, lambda x: x.startswith(">"))
	for k in groups:
		k = k.next()[1:].strip()
		data = []
		for line in groups.next():
#			print line
			if line.strip() != "":
				v = line.strip().split("\t")
				data.append(v)		
		d[k] = data
			
for item in l:
	if item in d:
		print item + "\t" + d[item][0][1]
