##########################################################################################
## to use in binning pandakiller assembled samples into seqfilter parsed tag directories############################################################################################

import sys
from Bio import SeqIO

names = []
tags = open(sys.argv[1], 'rU')
for record in SeqIO.parse(tags, "fasta"):
	names.append(record.id.split(' ')[0])
#print names

ids = []
reads = []
assemb = open(sys.argv[2], 'rU')
for line in SeqIO.parse(assemb, "fastq"):
	lexemes = line.id.rsplit(':', 1)
	ids.append(lexemes[0])
	reads.append(line.seq)

dict_assemb = dict(zip(ids, reads))

output = open(sys.argv[3], 'w')
drop = open(sys.argv[4], 'w')
for item in names:
	if item in dict_assemb:	
		output.write('>%s\n' % (item))
		output.write('%s\n' % (dict_assemb[item]))
	else:
		drop. write('%s\n' % (item))
	
