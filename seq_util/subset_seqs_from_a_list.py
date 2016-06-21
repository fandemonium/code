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

for records in SeqIO.parse(open(sys.argv[2], 'rU'), 'fasta'):
	mock_id = records.id.strip().split()[0]
	if mock_id in l_hits:
		continue
	else:	
		print ">" + mock_id + "\n" + records.seq	
