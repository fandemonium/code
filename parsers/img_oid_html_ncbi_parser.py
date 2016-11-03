import sys
import os
import re

for lines in open(sys.argv[1], 'rU'):
	line = lines.strip().split()
	img_oid = line[0].split(".")[1]
	ncbi_str = re.split("'|=", line[5])
	print img_oid, ncbi_str[-2]
