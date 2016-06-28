import sys
import re

for n, lines in enumerate(open(sys.argv[1], 'rU')):
	if n == 0:
		continue
	else:
		line = lines.strip().split("\t")
		hits = line[1]
		ID = hits.split("|")[1]
		start = int(line[8])
		end = int(line[9])
		if end - start > 0:
			print ID + " " + str(start) + "-" + str(end)
		else:
			 print ID + " " + str(end) + "-" + str(start) 
