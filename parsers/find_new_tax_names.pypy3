## sys.argv[1]: /mnt/home/yangfan1/databases/mcrA/mcrA_ref_tax.hier
## generated from: cut -f 2 mcrA_ref.taxonomy > mcrA_ref_tax.hier
## sys.argv[2]: /mnt/research/rdp/public/RDPTools/classifier/samplefiles/new_trainset_db_taxid.txt 

import sys

def get_uniq_tax_name(new_taxa):
	l = []
	for lines in open(new_taxa, 'rU'):
		line = lines.strip()[:-1]  ## remove trailing ';'
		lexemes = line.split(";")[:-1]   ## remove species from list
		l.extend(lexemes)
	new = set(l)
	return new

def db_tax_name(db_taxa):
	l = []
	for lines in open(db_taxa, 'rU'):
		line = lines.strip().split('*')
		db = line[1]
		l.append(db)
	new = set(l)
	return new

names = get_uniq_tax_name(sys.argv[1])
db_names = db_tax_name(sys.argv[2])

for item in names:
	if item in db_names:
		pass
	else:
		print(item)
	
