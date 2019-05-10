import sys
from Bio import SeqIO

d = {}
for line in open(sys.argv[1], 'rU'):
	line = line.strip().split('\t')
	ID = line[0]
	file = line[1]
	if file in d:
		d[file].append(ID)
	else:
		d[file]=[ID]

#for key in d:
#	print key + ' : ' + str(len(d[key]))

seqs = open(sys.argv[2])
seq_d = SeqIO.to_dict(SeqIO.parse(seqs, 'fasta'))

for key in d:
	out = "%s.fasta" % key
	f = open(out, 'w')
	for item in d[key]:
		SeqIO.write(seq_d[item], f, "fasta")
