import sys
import re
from Bio import Entrez

Entrez.email = "fyang@iastate.edu"

d = {}
for lines in open(sys.argv[1],'rU'):
	lines = lines.replace('"', '').strip().split("\t")
	oid = lines[0]
	org = lines[2]
	if oid not in d:
		d[oid] = org	
	else:
		d[oid].append(org)

for item in d:	
	handle = Entrez.esearch(db="genome", term=d[item])
	record = Entrez.read(handle)
	handle2 = Entrez.elink(dbfrom="genome", db="nuccore", id=record["IdList"])
	record2 = Entrez.read(handle2)
	print record2
