##python /mnt/data3/fan/code/parsers/img_oid_html_ncbi_parser.py oid_to_ncbi_to_ignore_removed.txt

import sys
import os
import re

exclude = ["href", "ncbi", "onclick"]

d = {}
for lines in open(sys.argv[1], 'rU'):
	line = re.split("val=|\'", lines)
	img_oid = line[0].split(".")[1]
	l = []
	for element in line:
		if all(x not in element for x in exclude):
			l.append(element)
	d[img_oid] = l

for keys in d:
	if "000001" in d[keys][0]:
		temp = list(d[keys][0])
		temp[-1] = "0"
		print(keys + "\t" + "".join(temp))
	else:
		print(keys + "\t" + d[keys][0])

