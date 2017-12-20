import os
import sys
import gzip
from Bio import SeqIO

file_name = sys.argv[1]
if ".gz" in file_name:
	f = gzip.open(file_name)
else:
	f = open(file_name, 'rU')
	
for records in SeqIO.parse(f, "fastq"):
	records.id = file_name.strip() + ":" + records.id.strip()
#	print records.id
#	SeqIO.write(records, out, 'fasta')
	print ">" + records.id + '\n' + records.seq
