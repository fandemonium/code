## take file names like this: FM_16s_2_TGAGTCACTGGT_assembled.test.fa to S_2|[sequence index] ##

import os
import sys
import re
from Bio import SeqIO

f = sys.argv[1]
out = open(sys.argv[2], 'w')

n = 0
for records in SeqIO.parse(open(f, 'rU'), "fasta"):
	n = n + 1
	records.id = 'S_' + re.split('-|\.|_', f)[2] + '|' + str(n)
	records.name = records.id
	records.description = records.id
	SeqIO.write(records, out, 'fasta')

