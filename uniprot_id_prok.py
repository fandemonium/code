## input: anything resembles /Users/metagenomics/Documents/Databases/uniprotKB_taxa.txt
## for virus, bacteria, archaea, and fungi
import sys
import os
import re

for line in open(sys.argv[1]):
	line = line.rstrip()
	lexeme = line.split("\t")
	id = lexeme[0]
	tax = lexeme[-1]
	domain = re.split("[|, |'|]", tax)
	#print domain[1]
	if domain[1] != "Eukaryota":
		print "%s\t%s" % (id, domain[1])
	if len(domain) != 3 and "Eukaryota" in domain[1] and "Fungi" in domain[5]:	
		print "%s\t%s" % (id, domain[5])
