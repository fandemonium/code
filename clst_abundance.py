#!/usr/bin/python
## part 2 of cdhit cluster parsing. use on outputs from cdhit_clst_parser.py as ##input 

import sys
import os
import re

f = open(sys.argv[1], 'rU')

ln = []
id = []
contig = []
for line in f:
	line = line.rstrip()
	lexeme = line.split("\t")
	ln.append(int(lexeme[0]))
#print ln
	if len(lexeme) != 1:
		id.append(lexeme[1])
	        contig.append(lexeme[2])

l = []
for x, y in zip(ln, ln[1:]):
	l.append(y-x-1)

m = zip(id, contig, l)
for (a, b, c) in m:
	print "%s\t%s\t%s" % (a, b, c)
