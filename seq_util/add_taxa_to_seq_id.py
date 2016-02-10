## sys.argv[1]: ~/databases/mcrA/mcrA_ref_fixed.taxonomy 
## sys.argv[2]: ~/databases/mcrA/mcrA_refs_no_dup.fa

import sys
from Bio import SeqIO

d = {}
for lines in open(sys.argv[1], 'rU'):
	lines = lines.strip()[:-1].split("\t")
	seq_id = lines[0]
	d[seq_id] = "Root;" + lines[1]

out = open(sys.argv[3], 'w')
for records in SeqIO.parse(open(sys.argv[2], 'rU'), "fasta"):
	if records.id in d.keys():
		records.id = records.id + ' ' + d[records.id]
		records.name = ""
		records.description = ""
		SeqIO.write(records, out, 'fasta')	
	else:
		print "id not found"
	
