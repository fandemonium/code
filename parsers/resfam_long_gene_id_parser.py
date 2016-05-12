### input:
#AB008454.1.gene1.p01
#AB061794.1.gene2.p01
#AB061794.1.gene7.p01
#
### output:
#


import sys
import re
from Bio import Entrez
from Bio import SeqIO

database = "nuccore"
Entrez.email = "fan.michelle.yang@gmail.com"

error_out = open("gene_id_not_found.txt", 'w')

d = {}
for lines in open(sys.argv[1], 'rU'):
	line = lines.strip()
	lexemes = re.split("\.|\|", line)
	if line.startswith("gi"):
		ID = lexemes[1]
	else:
		ID = lexemes[0]
	d[line]=ID

missing = {}
for key, acc in d.items():
	try:
		handle = Entrez.efetch(db = database, rettype = "gb", id = acc)
		records = []
		records.append(handle.read())
		for item in records:
			info = item.split("\n")
			for i in info:
				if "taxon" in i:
					print "%s\t%s\t%s" % (key, acc, re.split(":|\"", i.strip())[-2])
	except Exception:
		missing[key] = acc
		pass

for items in missing:	
	error_out.write("%s\t%s\n" % (items, missing[items]))
