import os
import sys

f = sys.argv[1]

for lines in open(f, 'rU'):
	lines = lines.strip()
	add = f + '\t' + lines
	print(add)
