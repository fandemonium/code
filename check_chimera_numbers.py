import sys
import os
import re
from collections import Counter

good = open(sys.argv[1], 'rU')
chim = open(sys.argv[2], 'rU')
assem = open(sys.argv[3], 'rU')

d_good = {}
for lines in good:
	lines = lines.strip()
	lexemes = re.split("_|:", lines)
	file_id = lexemes[0]
	number = int(lexemes[-1])
	d_good[file_id] = number
        good_c = Counter(d_good)
#print d_good

d_chim = {}
for lines in chim:
	lines = lines.strip()
	lexemes = re.split("_|:", lines)
	file_id = lexemes[0]
	number = int(lexemes[-1])
	d_chim[file_id] = number
	chim_c = Counter(d_chim)

d_assem = {}
for lines in assem:
	lines = lines.strip()
	lexemes = re.split("_|:", lines)
	file_id = lexemes[0]
	number = int(lexemes[-1])
	d_assem[file_id] = number
	assem_c = Counter(d_assem)

compare = good_c + chim_c - assem_c
print dict(compare)
#if output is "{}", everything sums up to original binned assembled reads. 
