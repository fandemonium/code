## adopted from Aaron Sharp's code. Modified to work with tab delimited file. 

import sys

if len(sys.argv) != 2:
	print("USAGE: python revcomp_rdp_format.py RPD_MAPPING_FILE.txt > RPD_MAPPING_FILE_REV.txt")
	sys.exit()

fh = open(sys.argv[1])

for lines in fh:
	lines = lines.strip()
	lexemes = lines.split('\t')
	tags = lexemes[0]
	samples = lexemes[1]
	output = "";
	for i in range(0, len(tags)):
		if (tags[i] == 'c' or tags[i] == 'C'):
			output += "G"
		if (tags[i] == 'g' or tags[i] == 'G'):
			output += "C"
		if (tags[i] == 't' or tags[i] == 'T'):
			output += "A"
		if (tags[i] == 'a' or tags[i] == 'A'):
			output += "T"
	print('%s\t%s\t' %(output[::-1], samples))
