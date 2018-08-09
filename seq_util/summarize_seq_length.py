import sys
from Bio import SeqIO

for records in SeqIO.parse(open(sys.argv[1]), 'fasta'):
	print records.id + "\t" + str(len(records.seq))
