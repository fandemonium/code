import sys
import re
from itertools import groupby

def group_separator(line):
	return line.startswith("[1] \"Processing")

def hasNumbers(input_string):
	return any(char.isdigit() for char in input_string)

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
#				elif lines.startswith("   "): # for "sample_information_bayes_factors_order_restricted_H.txt"
				elif hasNumbers(lines) is True: # for "bacteria_core_genus_bayes_factors_order_restricted_H.txt" and abov file
					bf = lines.strip().split()[-1]
					d[col].append(bf)
			except:
				pass	

	for item in d:
		print item + "\t" + "\t".join(d[item])
