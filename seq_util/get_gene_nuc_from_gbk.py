import sys
from Bio import SeqIO

#eg.,P450
gene = sys.argv[2]

for rec in SeqIO.parse(open(sys.argv[1]), "genbank"):
	for feature in rec.features:
		if feature.type == "CDS":
			if gene in feature.qualifiers['product'][0]:
				gene_id = feature.qualifiers.values()[0][0].split("|")[1]
				print ">%s:%s:%s\n%s" % (gene_id, feature.qualifiers['product'][0], rec.name, feature.location.extract(rec).seq)
