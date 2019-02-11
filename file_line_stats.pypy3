import sys
import re
import os

files = sys.argv[1]

def line_stats(bind_ss):
	l = []
	for lines in bind_ss:
		line = lines.strip().split('\t')
		l.append(len(line))
	return 'max line length: ' + str(max(l)), 'min line length: ' + str(min(l))

print(line_stats(open(f, 'rU')))

