import sys
from Bio import SeqIO

for rec in SeqIO.parse(open(sys.argv[1]), "genbank"):
	if "P450" in rec.features:
		print fature.location.extract(rec).seq
