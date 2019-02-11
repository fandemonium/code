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
	if cigar.endswith("S"):
		continue
	elif "S" in cigar:
		five_prime = cigar.split("S")
		if int(five_prime[0]) <= 2:
			print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (gene, sets, f_r, flag, pos, qual, cigar))
	else:
			print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (gene, sets, f_r, flag, pos, qual, cigar))
		
