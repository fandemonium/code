import sys
import os
import numpy

l = []
for lines in open(sys.argv[1], 'rU'):
	lines = lines.strip()
	lexeme = lines.split(':')
	counts = int(lexeme[-1])
	l.append(counts)
print(sum(l))
