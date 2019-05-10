import sys
import os

d = {}
with open(sys.argv[1], 'rU') as f:
	next(f)
	for lines in f:
		line = lines.strip().split('\t')
		kingdom = line[0]
		phylum = line[1]
		oid = line[-1]
		if kingdom == "Bacteria":
			if phylum in d:
				d[phylum].append(oid)
			else:
				d[phylum]=[oid]

for key in d:
	print(key +": "+str(d[key]))
