import sys
from Bio import SeqIO

for rec in SeqIO.parse(open(sys.argv[1]), "genbank"):
	for feature in rec.features:
		if feature.type == "CDS":
#			print feature
			gene_id = feature.qualifiers.values()[0][0].split(":")[1]
			print ">%s:%s\n%s" % (gene_id, rec.name, feature.location.extract(rec).seq)

