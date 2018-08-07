import sys
from Bio import SeqIO

d = {}
for records in SeqIO.parse(open(sys.argv[1]), 'fasta'):
	if records.id not in d:
		d[records.id] = [records.seq]
	else:
		d[records.id].append(records.seq)

for item in d:
	l = {}
	for i, v in enumerate(d[item]):
		l[i] = len(v)
	for stuff in l:
		if l[stuff] == max(l.values()):
			print ">" + item + "::" + str(stuff) + "\n" + d[item][stuff]
