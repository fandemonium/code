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

l = []
for lines in open(sys.argv[1], 'rU'):
	line = lines.strip()
	lexemes = re.split("\.|\|", line)
	if line.startswith("gi"):
		ID = lexemes[1]
	else:
		ID = lexemes[0]
	l.append(ID)

database = "nuccore"
Entrez.email = "fan.michelle.yang@gmail.com"

error_out = open("gene_id_not_found.txt", 'w')
missing = []
for acc in l:
	try:
		handle = Entrez.efetch(db = database, rettype = "gb", id = acc)
		records = []
		records.append(handle.read())
		for item in records:
			line = item.split("\n")
			for i in line:
				if "taxon" in i:
					print acc, re.split(":|\"", i.strip())[-2] 
	except Exception:
		missing.append(acc)
		pass
error_out.write("\n".join(missing))	
	
