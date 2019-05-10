#! /usr/bin/env python

#Parser for blast -m 8 or blast+ -m 6 and 7 output file with description inserted

import sys
import numpy
import re

##Query id, query start, query end, qurey length, Subject id, subject start, subject end, alignment length, % identity, e-value,bit score

d = {}
for lines in open(sys.argv[1], 'rU'):
	lexemes = lines.strip().split('\t')
	asv_id = lexmes[0]
	asv_len = float(lexemes[3])
	matching_contig = lexemes[4]
	aln_len = float(lexemes[7])
	pident = float(lexemes[8])
	adj_pident = pident * aln_len / asv_len
	if asv_id not in d:
		d[asv_id] = {matching_contig: adj_pident}
	else:
		d[asv_id].update({matching_contig: adj_pident})

# strain desc file in the format of:
# strain	species strain	contigs
orgs = {}
for strings in open(sys.argv[2], 'rU'):
	string = string.strip().split("\t")
	strain = string[1]
	contig = string[2]
	if strain not in orgs:
		orgs[strain] =[contig]
	else:
		orgs[strin],append(contig)

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
		l3 = []
		for item in l2:
			for strain, contig in orgs.items():
				if item in contig:
					l3.append(strain)
		print(asv + '\t' + str(best) + '\t' + "|".join(l3))
