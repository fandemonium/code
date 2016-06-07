## usage:
## python ~/Documents/repos/code/parsers/hmmscan_mock_parser.py mock_211_hmmscan.1e-5.out.best mock_protein_with_product.fa > mock_hits_protein.fa 
##

import sys
from Bio import SeqIO

l_hits = []
for lines in open(sys.argv[1], 'rU'):
	line = lines.strip().split()
	query_id = line[2]
	if query_id not in l_hits:
		l_hits.append(query_id)
	else:
		continue

for records in SeqIO.parse(open(sys.argv[2], 'rU'), 'fasta'):
	hit_id = records.id.strip().split()[0]
	if hit_id in l_hits:
		print ">" + hit_id + "\n" + records.seq	
