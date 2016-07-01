import sys
import re
from itertools import groupby

def group_separator(line):
	return line.startswith("[1] \"Processing")

f = open(sys.argv[1])

#for lines in f:
#	print group_separator(lines)

for param, group in groupby(f, group_separator):
#	print param, list(group)
	d = {}
	if param:
		for string in group:
			col = string.strip().split("\"")[3]
	if not param:
		for lines in group:
			try:
				if lines.startswith("[1] "):
					order = lines.strip().split("\"")[1]
					d[col]=[order]
				elif lines.startswith("   "):
					bf = lines.strip().split()[-1]
					d[col].append(bf)
			except:
				pass	

	for item in d:
		print item + "\t" + "\t".join(d[item])
