import sys
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

blast = sys.argv[1]
fa = sys.argv[2]

d = {}
for lines in open(blast, 'rU'):
	lexemes = lines.strip().split("\t")
	contigs = lexemes[0]
	identity = lexemes[2]
	aln_len = lexemes[3]
	start = lexemes[6]
	end = lexemes[7]
	if int(aln_len) >= 900:
		d[contigs] = [start, end]

for records in SeqIO.parse(open(fa), "fasta"):
	if records.id in d.keys():
		print ">" + records.id + "_position_" + ":".join(d[records.id])
		trunk = SeqFeature(FeatureLocation(int(d[records.id][0]), int(d[records.id][1])), type="gene", strand=1)
		print records.seq[trunk.location.start:trunk.location.end]

