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
