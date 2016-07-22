import sys
import re

for lines in open(sys.argv[1], 'rU'):
	line = lines.strip().split("\t")
	primers = line[0].split("_")
	if len(primers) == 5:
		gene = primers[0]
		sets = primers[2][0:len(primers[2])-1]
		f_r = primers[2][-1:]
	else:
		gene = primers[0]
		sets = primers[3][0:len(primers[3])-1]
		f_r = primers[3][-1:]
	flag = line[1]
	pos = line[3]
	qual = line[4]
	cigar = line[5]
	matches = line[11]
	md = line[-2]
	if matches == "AS:i:0":
		if len(line) == 19:
			gaps = line[14]
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (gene, sets, f_r, flag, pos, qual, cigar, matches, gaps, md)
		else:	
			gaps = line[15]
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (gene, sets, f_r, flag, pos, qual, cigar, matches, gaps, md)
		
