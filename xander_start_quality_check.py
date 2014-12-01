import os
import sys
import gzip
from Bio import SeqIO
import numpy

meta_gz = gzip.open(sys.argv[1], 'rU')
#seqs_dict = SeqIO.to_dict(SeqIO.parse(meta_gz, "fastq"))
seqs_dict = {}
for records in SeqIO.parse(meta_gz, "fastq"):
	seqs_dict[records.id] = records.letter_annotations
#print seqs_dict


gene_starts = open(sys.argv[2], 'rU')
id_to_grab = {}
for lines in gene_starts:
	lines = lines.strip()
	lexemes = lines.split('\t')
	seq_id = lexemes[1]
	id_to_grab[seq_id] = seq_id
#print len(id_to_grab)

for item in id_to_grab:
	if item in seqs_dict:
		dictavg = numpy.mean([numpy.mean(x) for x in seqs_dict[item].values()])
		dictmin = numpy.min([numpy.min(x) for x in seqs_dict[item].values()])
		print "%s has avg Q = %s and min Q = %s" % (item, dictavg, dictmin)
	else:
		print "%s can't be found!" % (item)
