import os
import sys
if len(sys.argv) != 2:
	print "USAGE: python MiSeq_rdptool_map_parser.py ANL_MAPPING_FILE.txt > RDP_MAPPING_FILE.txt"
	sys.exit()

def replace_space(SN):
	if " " in SN:
		SN.replace(" ", "_")
	else:
		continue

with open(sys.argv[1], 'r') as f:
	next(f)
	for lines in f:
		lines = lines.strip()
		lexemes = lines.split('\t')
		sample = lexemes[0]
		file_name = replace_space(sample)
		tag = lexemes[1]
		print '%s\t%s' % (tag, file_name)

