import sys
from Bio import SeqIO
import re

## read in .gff file
gff = open(sys.argv[1], 'rU')
## read in gene fna file
fna = SeqIO.parse(open(sys.argv[2]), "fasta")

firstline = gff.readline()

d = {}
for line in gff:
	lexeme = line.strip().split("\t")
	gene_type = lexeme[2]
	start_pos = lexeme[3]
	end_pos = lexeme[4]
	strand = lexeme[6]
	genome_oid = sys.argv[1].split(".")[0]
	if len(lexeme) < 9:
		continue
	else:
		info = lexeme[-1].strip().split(";")
		gene_id = info[0].split("=")[1]
		if "product=" not in lexeme[-1]:
			product = "NA"
			d[gene_id] = [genome_oid, gene_type, start_pos, end_pos, strand, product]
		else:
			matching = [x for x in info if 'product=' in x][0]
			product = matching.split("=")[1]
			d[gene_id] = [genome_oid, gene_type, start_pos, end_pos, strand, product]

l = []
for item in d:
	if d[item][1] == "rRNA" and "16S" in d[item][-1] and "+" in d[item][-2]:
		l.append(item)
	elif len(l) == 0:
		if d[item][1] == "rRNA" and "16S" in d[item][-1] and "-" in d[item][-2]:
			l.append(item)

## only take the first 16S gene locus_tag
## the output header is in the format of:
## >img_genome_OID::gene_locus_tag::genedescription
l_err = []
if len(l) >= 1:
	for records in fna:
		for gid in l:
			if records.id == gid:
				print(">"+genome_oid+"::"+gid+"::"+records.description)
				print(records.seq)
else:
	error = open(sys.argv[3], 'w')
	l_err.append(genome_oid)
	error.write("\n".join(l_err))
