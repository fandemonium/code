### usage: python ~/repos/code/parsers/gene_feature_parser.py ecoli_salm_gene_features.txt > ecoli_salm_all_gene_features_w_positions.txt
import sys
import re

def get_positions(feature):
	if "complement" in feature:
		start = re.split("\(|\.\.|\)", line[-1])[1]
		end = re.split("\(|\.\.|\)", line[-1])[2]
		return "%s\t%s\t%s" % (start, end, "-")
	else:
		start = re.split("=|\.\.|\]", line[-1])[1]
		end = re.split("=|\.\.|\]", line[-1])[2]
		return "%s\t%s\t%s" % (start, end, "+")

	
for lines in open(sys.argv[1], 'rU'):
	line = lines.strip().split(" ")
	if len(line) == 4:
		acc = re.split("\||\.3", line[0])[1]
		gene = re.split("=|\]", line[1])[1]
		locus_tag = re.split("=|\]", line[2])[1]
		print("%s\t%s\t%s\t%s" % (acc, gene, locus_tag, get_positions(line[-1])))
	else:
		acc = re.split("\||\.3", line[0])[1]
		locus_tag = re.split("=|\]", line[1])[1]
		print("%s\t%s\t%s\t%s" % (acc, "NA", locus_tag, get_positions(line[-1])))
		
