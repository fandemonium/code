import sys
from Bio import SeqIO
import numpy as np

seq = open(sys.argv[1])

d = {}
for record in SeqIO.parse(seq, "fastq"):
	d[record.id] = record.letter_annotations["phred_quality"]
#print len(d) 

def pe(Q):
	n = float(i)/10
	p = np.power(10, -n)
	return p

l = []	
for item, value in d.iteritems():
#	d[item] = [pe(i) for i in value[:-1]]
#	print item + ": " + str(np.sum(d[item]))
#	print item + ": " + str(np.min(d[item]))
	if np.min(d[item]) >= 20:
		l.append(np.min(d[item]))
print len(l)
	
