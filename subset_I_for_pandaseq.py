import sys
import gzip
from Bio import SeqIO

l_id = []
assem = gzip.open(sys.argv[1], 'rU')
for records in SeqIO.parse(assem, 'fastq'):
	l_id.append(records.id)
#print len(l_id)

tags = open(sys.argv[2], 'rU')
tag_dict = SeqIO.to_dict(SeqIO.parse(tags, "fastq"))
#print tag_dict

out = open(sys.argv[3], 'w')
for item in l_id:
	SeqIO.write(tag_dict[item], out, "fastq")
