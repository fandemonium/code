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
	if param:
		for string in group:
			col = string.strip().split("\"")[3]
	if not param:
		for lines in group:
			lines = lines.strip()
			try:
				lexeme = re.split(" : ", lines)
				bf = lexeme[1]
				print(col + "\t" + bf)
			except:
				pass
