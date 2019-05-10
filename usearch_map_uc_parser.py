import os
import sys
import numpy

l = []
for lines in open(sys.argv[1], 'rU'):
	lines = lines.strip()
	lexemes = lines.split('\t')
	seq = lexemes[-2] + ';' + 'barcodelabel=%s' % sys.argv[1].split('.')[0]
	print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (lexemes[0],lexemes[1], lexemes[2], lexemes[3], lexemes[4], lexemes[5], lexemes[6], lexemes[7], seq, lexemes[9])) 
