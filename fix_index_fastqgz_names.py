##fixing index fastq.gz seq names to match RDP assembler's seq names###

import sys
import gzip
from Bio import SeqIO

if len(sys.argv) != 3:
	print("USAGE: python fix_index_fastqgz_names.py XXX_I.fastq.gz FIXED_I.fastq")
	sys.exit()

f = gzip.open(sys.argv[1], 'rU')
output = open(sys.argv[2], 'w')

for records in SeqIO.parse(f, 'fastq'):
	records.id = records.id.split(' ')[0] + ":0"
	records.description = records.description.split(' ')[0] + ":0"
	records.name = records.name.strip() + ":0"
#	print records
	SeqIO.write(records, output, "fastq")	
