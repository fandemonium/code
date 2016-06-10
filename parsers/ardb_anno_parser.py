## input file: anything resembles /Users/metagenomics/Documents/Fan/scratch/xander_701/Asp/nucl_cdhit.fasta.clstr

import sys
import os
import re
from itertools import groupby

def group_matches(ardb_anno):
	f = open(ardb_anno)
	citer = (x[1] for x in groupby(f, lambda line: line[0] == ">"))
	anno = {}
	for header in citer:
		mock_id = header.next()[1:].strip().split(">")[0]
		for lines in citer.next():
			string = lines.strip()
			fields = string#[0]
			anno[mock_id] = [fields]
		yield anno

ardb_anno_f = sys.argv[1]
d = group_matches(ardb_anno_f)
for item in d:
	print d[item]	

