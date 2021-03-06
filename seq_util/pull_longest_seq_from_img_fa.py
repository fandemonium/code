import sys
from Bio import SeqIO
import operator

# 1. get genome img_oid from the genecart text file
# 2. create gene sequence dictionary
# 3. add genome img_oid to the gene sequence dictionary
# 4. for genes from the same organism, pull the longest sequence out


gene_cart = open(sys.argv[1], 'rU')
firstline = gene_cart.readline()

oid_dict = {}
for lines in gene_cart:
	lexeme = lines.strip().split("\t")
	gene_id = lexeme[0]
	img_oid = lexeme[3]
	if img_oid not in oid_dict:
		oid_dict[img_oid] = [gene_id]
	else:
		oid_dict[img_oid].append(gene_id)

seq_dict = SeqIO.to_dict(SeqIO.parse(open(sys.argv[2]), 'fasta'))
MIN_LENGTH = int(sys.argv[3])

no_genes_out = open(sys.argv[4], 'w')
l = []
for oid in oid_dict:
	gene_dict = {}
	for gene in oid_dict[oid]:
		gene_dict[gene] = seq_dict[gene]
        if len(gene_dict) > 0:
                longest_seq_key = max(gene_dict.iteritems(), key=operator.itemgetter(1))[0]
		if len(gene_dict[longest_seq_key]) >= MIN_LENGTH:
                	print ">"+ oid + "::" +  longest_seq_key + "::" + gene_dict[longest_seq_key].description + "\n" +gene_dict[longest_seq_key].seq
	        else:
	                l.append(oid)
	else:
		l.append(oid)
no_genes_out.write("\n".join(l))

