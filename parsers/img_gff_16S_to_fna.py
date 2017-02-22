import sys
from Bio import SeqIO
import re

## read in .gff file

gff = open(sys.argv[1], 'rU')

firstline = gff.readline()

for line in gff:
	lexeme = line.strip().split("\t")
	locus_tag = lexeme[-1].split(";")[1].split("=")[1]
	product = lexeme[-1].split(";")[2].split("=")[1]
	print product
	if "16S" in product:
		print product, locus_tag
