import sys
import re
from Bio import SeqIO

def revcomp(fh):
	output = "";
	for i in range(0, len(fh)):
		if (fh[i] == 'c' or fh[i] == 'C'):
			output += "G"
		if (fh[i] == 'g' or fh[i] == 'G'):
			output += "C"
		if (fh[i] == 't' or fh[i] == 'T'):
			output += "A"
		if (fh[i] == 'a' or fh[i] == 'A'):
			output += "T"
	return output[::-1]

for records in SeqIO.parse(open(sys.argv[1]), "fasta"):
	name = records.id
	seq = revcomp(records.seq)
	print name + "\t" + seq
