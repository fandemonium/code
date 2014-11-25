import sys
import os
import re

n = -1 
for seqs in open(sys.argv[1], 'rU'):
	if seqs.startswith('>M'):
		n = n + 1
		seq_id = re.split(">| ", seqs)[1]
		print '%s %s' % (n, seq_id)
		
