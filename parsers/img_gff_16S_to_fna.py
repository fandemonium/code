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
		info = lexeme[-1].split(";")
		locus_tag = info[1].split("=")[1]
		if len(info) == 2:
			product = "NA"
			d[locus_tag] = [genome_oid, gene_type, start_pos, end_pos, strand, product]
		else:
			product = info[2].split("=")[1]
			d[locus_tag] = [genome_oid, gene_type, start_pos, end_pos, strand, product]

l = []
for item in d:
	if d[item][1] == "rRNA" and "16S" in d[item][-1] and "+" in d[item][-2]:
		l.append(item)

## only take the first 16S gene locus_tag
## the output header is in the format of:
## >img_genome_OID::gene_locus_tag::genedescription
for records in fna:
	if l[0] in records.description:
		print ">"+genome_oid+"::"+l[0]+"::"+records.description
		print records.seq
