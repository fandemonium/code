import os
import sys
import re
from Bio import SeqIO
from Bio import Entrez

d = {}
for n, line in enumerate(open(sys.argv[1], 'rU')):
	if n > 0:
		row = line.strip()
		lexemes = re.split("\||\t", row) 
		assay = lexemes[5]
		gid = lexemes[1]
		if assay in d:
			d[assay].append(gid)
		else:
			d[assay]=[gid]

for key in d:
	out = "%s.txt" % key
	f = open(out, 'w')
	for item in d[key]:
		f.write("%s\n" % item)
