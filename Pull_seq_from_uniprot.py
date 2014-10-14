import sys
import os
from Bio import SeqIO
import re

l_id = []
l_seq = []

s = open(sys.argv[1], 'r')
for line in SeqIO.parse(s, 'fasta'):
    name, seq = line.id, line.seq.tostring()
#    id_long = re.split("\|", name)[2]
    l_id.append(re.split("\|", name)[1])
    l_seq.append(seq)
#    print id_long 
#print l_seq
# '|' itself is a nulti-divider seperater. need \ to escape it to be used as a divider itself.
#print len(l_id)
dict_seq = dict(zip(l_id, l_seq))

id_to_grab = []
with open(sys.argv[2]) as f:
    next(f)
    for line in f:
       	line = line.strip()
	lexemes = re.split(" |_|\n", line)
#        lexemes = re.split("\t|_|\n", line)
        gene_id = lexemes[1]
        id_to_grab.append(gene_id)
#	print gene_id

out = open(sys.argv[3], 'w')
for item in id_to_grab:
    out.write('>%s\n' % item)
#    out.write('>%s\t%s\n' % (item, id_long))
    out.write('%s\n' % dict_seq[item])
