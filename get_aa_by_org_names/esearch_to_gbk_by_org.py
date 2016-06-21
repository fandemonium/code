import sys
import re
from Bio import Entrez

Entrez.email = "fyang@iastate.edu"

l = []
for lines in open(sys.argv[1],'rU'):
	lines = lines.replace('"', '').strip().split("\t")
	org = lines[2]
	if org in l:
		continue
	else:
		l.append(org)

for item in l:	
	handle = Entrez.esearch(db="genome", term=item)
	record = Entrez.read(handle)
	print record
