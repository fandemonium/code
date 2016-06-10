import sys
from Bio import SeqIO

l_hits = []
for n, lines in enumerate(open(sys.argv[1], 'rU')):
	if n == 0:
		continue
	else:
		line = lines.strip().split()
		hit_id = line[0]
		if hit_id not in l_hits:
			l_hits.append(hit_id)
		else:
			continue

d = {}
for records in SeqIO.parse(open(sys.argv[2], 'rU'), 'fasta'):
	seq_id = records.id.strip()
	seq = records.seq
	if seq_id not in d:
		d[seq_id] = seq
	else:
		continue

for item in l_hits:
	print ">%s" % (item)
	print d[item]
