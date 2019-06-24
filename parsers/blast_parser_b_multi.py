#! /usr/bin/env python

#Parser for blast -m 8 or blast+ -m 6 and 7 output file with description inserted

import sys
import numpy
import re

##Query id, query start, query end, qurey length, Subject id, subject start, subject end, alignment length, % identity, e-value,bit score

d = {}
for lines in open(sys.argv[1], 'r'):
	lexemes = lines.strip().split('\t')
	asv_id = lexemes[0]
	asv_len = float(lexemes[3])
	matching_contig = lexemes[4]
	aln_len = float(lexemes[7])
	pident = float(lexemes[8])
	adj_pident = pident * aln_len / asv_len
	if asv_id not in d:
		d[asv_id] = {matching_contig: adj_pident}
	else:
		d[asv_id].update({matching_contig: adj_pident})

for asv in d:
	l = []
	for key, val in d[asv].items():
		l.append(val)
	if max(l) >= 95:
		best = max(l)
	l2 = []
	for key, val in d[asv].items():
		if val == best:
			l2.append(key)
	if len(l2) > 0:
		for items in l2:
			print(asv + '\t' + str(best) + '\t' + items)
