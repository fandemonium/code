import sys
import re
from itertools import groupby

def primerset_groups(line):
	return line.strip().endswith("Pair:")

f = sys.argv[1]
gene = f.split(".txt")[0]
#for lines in f:
#	print primerset_groups(lines)

for group, lines in groupby(open(f), primerset_groups):
	d = {}
	if not group:
		for string in lines:
			if string.startswith("Percent Seq Coverage:"):
				coverage = string.strip().split(" ")[-1]
				d[gene] = [coverage]
			elif string[0].isdigit():
				d[gene].append(string)
	for item in d:
		print item + "\t" + str(len(d[item])-1)+ "\t" + d[item][0] 	

