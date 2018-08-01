# usage: python ~/Documents/repos/code/seq_util/get_seq_islands.py usda110_vs123_unique_islands_1k.txt usda110_seq.txt "usda110" > usda110_vs123_unique_islands_1k.fa
# input usda123_seq.txt are fa file without contig headers (ie, > lines)

import sys
import numpy as np

def extract_seqs(seq_file, left_pos, right_pos):
	seqs = []
	seq_no_header = open(seq_file, 'rU')
	for lines in seq_no_header:
		line = lines.strip()
		seqs.append(line)
	seq = ''.join(seqs)
	s = seq[left_pos:right_pos]
#	print seq
	return s

f = open(sys.argv[1], 'rU')
seq_txt = sys.argv[2]

for lines in f.readlines()[1:]:
	line = lines.strip().split("\t")
	left = np.abs(int(line[0]))
	right = np.abs(int(line[1]))
	print ">" + sys.argv[3] + "_islands::" + str(left+1) + "-" + str(right-1)
	print extract_seqs(seq_txt, left, right-1)

