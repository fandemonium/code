import os
import sys
from Bio import SeqIO

out = open(sys.argv[2], 'w')
for records in SeqIO.parse(open(sys.argv[1], 'rU'), "fasta"):
	records.id = records.id.strip() + '%s' % sys.argv[1].split('.')[0]
	records.name = records.id
	records.description = records.id
	SeqIO.write(records, out, 'fasta')
