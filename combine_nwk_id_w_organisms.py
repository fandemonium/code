import sys
import os
from Bio import SeqIO
import re

l_id = []
l_long_id = []

s = open(sys.argv[1], 'r')
for line in s:
    if line.startswith(">"):
        l_long_id.append(re.split("\||=", line)[3])
        l_id.append(re.split("\|", line)[1])
#	print re.split("\||=", line)[3]
# '|' itself is a nulti-divider seperater. need \ to escape it to be used as a divider itself.
#print len(l_id)
dict_id = dict(zip(l_id, l_long_id))

id_to_grab = []
with open(sys.argv[2]) as f:
    next(f)
    for line in f:
        lexemes = re.split(" |_|\n", line)
        gene_id = lexemes[1]
        id_to_grab.append(gene_id)
#	print gene_id
out = open(sys.argv[3], 'w')
for item in id_to_grab:
    out.write('%s\t%s\n' % (item,dict_id[item]))
