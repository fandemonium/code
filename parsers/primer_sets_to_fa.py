import sys
import re
from itertools import groupby

def revcomp(fh):
	output = "";
	for i in range(0, len(fh)):
		if (fh[i] == 'c' or fh[i] == 'C'):
			output += "G"
		if (fh[i] == 'g' or fh[i] == 'G'):
			output += "C"
		if (fh[i] == 't' or fh[i] == 'T'):
			output += "A"
		if (fh[i] == 'a' or fh[i] == 'A'):
			output += "T"
	return output[::-1]

def primerset_groups(line):
	return line.strip().endswith("Pair:")

f = sys.argv[1]
gene = f.split(".txt")[0]
#for lines in f:
#	print primerset_groups(lines)

d = {}
for group, lines in groupby(open(f), primerset_groups):
	if group:
		for string in lines:
			header = string.split(" ")[0]
	if not group:
		s = {}
		l = []
		for string in lines:
			if string.startswith("Percent Seq Coverage"):
				cov = string.strip().split(": ")[-1]
			elif string[0].isdigit():
				sets = string.strip()
				l.append(sets)
		if len(l) > 0 and len(l) == int(header):
			s[cov] = l
	if int(len(s)) > 0:
		if gene not in d:
			d[gene] = s
		else:
			d[gene].update(s)
for item in d:
	for keys in d[item]:
		if keys ==  max(d[item], key=d[item].get):
			for primers in d[item][keys]:
				val = re.split("seq=|}|\[|, |\]", primers)
				num = val[0].split(" ")[0]
				f = val[1]
				r = val[4]
				f_pos = val[-3]
				r_pos = val[-2]
				print ">%s_%s_%s%s_%s_%s" % (item, keys, num, "f",  f_pos, r_pos)
				print f
				print ">%s_%s_%s%s_%s_%s" % (item, keys, num, "r", f_pos, r_pos)
				print revcomp(r)
	
