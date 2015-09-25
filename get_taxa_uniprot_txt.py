import os
import sys
import re
a = []
f = sys.argv[1].split(".")[0]
for lines in open(sys.argv[1], 'rU'):
	lines = lines.strip()
	#if lines.startswith("AC"):
	#	ID = re.split(" |;", lines)[3]
	if lines.startswith("OC"):
		taxa = lines.partition(" ")[2].strip(" ")
		a.append(taxa)
print f + '\t' + " ".join(a)
