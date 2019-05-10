import os
import sys
from Bio import SeqIO

out = open(sys.argv[2], 'w')
#print sys.argv[1]
for records in SeqIO.parse(open(sys.argv[1], 'rU'), "fasta"):
	up = records.id.split(';')[-2]
	records.id = records.id.split(';')[0] + ';' + records.id.split(';')[1]# + ';barcodelabel=%s' % sys.argv[1].split('.')[0]
	records.name = records.id
	records.description = records.id
	if up != "up=chimera":
		SeqIO.write(records, out, 'fasta')
