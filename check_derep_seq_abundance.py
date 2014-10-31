import os
import sys
import numpy

l = []
for lines in open(sys.argv[1], 'rU'):
	if lines.startswith(">"):
		lexemes = lines.strip().split(';')
		seq_abun = int(lexemes[-1].split('=')[-1])
		l.append(seq_abun)
print sum(l)
