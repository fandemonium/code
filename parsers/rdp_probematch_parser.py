# rdp probe match file is usually really big, do subset first. eg
# grep -E "Escherichia|Enterococcus" 16s_515F806R_rdp_probematch.txt > FC_matches.txt
#
# usage: python ~/Documents/repos/code/parsers/rdp_probematch_parser.py FC_matches.txt > FC_matches_for_R.txt

import sys
import numpy

#d = {}
for lines in open(sys.argv[1], 'rU'):
	if lines.startswith("#"):
		continue
	else:
		line = lines.strip()
		lexemes = line.split(" ", 11)
		rdp_id = lexemes[0]
		f_dist = lexemes[1]
		f_end = lexemes[3]
		r_dist = lexemes[6]
		r_start = lexemes[7]
		desc = lexemes[-1]
#		d[rdp_id] = [f_dist, f_end, r_dist, r_start, desc]
		seq_len = int(r_start) - int(f_end) - 1
		print "%s\t%s\t%s" % (rdp_id, str(seq_len), desc)
