## input: anything resembles /Users/metagenomics/Documents/Databases/uniprotKB_taxa.txt
## for fungi only

import sys
import os
import re

for line in open(sys.argv[1]):
	line = line.rstrip()
	lexeme = line.split("\t")
	id = lexeme[0]
	tax = lexeme[-1]
	domain = re.split("[|, |'|]", tax)
	#print domain[4]
	if len(domain) != 3:	
		if "Fungi" in domain[5]:
			print "%s\t%s" % (id, domain[5])
