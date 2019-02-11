import sys
import os
import re

sample = open(sys.argv[1], 'rU')
for seqs in sample:
	if seqs.startswith(">M"):
		seq_id = re.split(">| ", seqs)[1]
		print(seq_id + "\t" + sys.argv[1].rsplit('.', 1)[0])
