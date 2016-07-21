import sys
import re

for lines in open(sys.argv[1], 'rU'):
	line = lines.strip().split(" ")
	acc = re.split("\||\.3", line[0])[1]
	gene = re.split("=|\]", line[1])[1]
	locus_tag = re.split("=|\]", line[2])[1]
	if "complement" in line[-1]:
		start = re.split("\(|\.\.|\)", line[-1])[1]
		end = re.split("\(|\.\.|\)", line[-1])[2]
		print "%s\t%s\t%s\t%s\t%s\t%s" % (acc, gene, locus_tag, start, end, "-")
	else:
		start = re.split("=|\.\.|\]", line[-1])[1]
		end = re.split("=|\.\.|\]", line[-1])[2]
		print "%s\t%s\t%s\t%s\t%s\t%s" % (acc, gene, locus_tag, start, end, "+")

