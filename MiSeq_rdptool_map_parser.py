import os
import sys

with open(sys.argv[1], 'r') as f:
	next(f)
	for lines in f:
		lines = lines.strip()
		lexemes = lines.split('\t')
		sample = lexemes[0]
		tag = lexemes[1]
		print '%s\t%s' % (tag, sample)

