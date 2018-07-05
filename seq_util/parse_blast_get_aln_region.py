import sys
from Bio import SeqIO

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

records.d = SeqIO.index(fa, "fasta")

print records.d
