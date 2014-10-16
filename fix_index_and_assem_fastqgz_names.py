import sys
import gzip
from Bio import SeqIO

f = gzip.open(sys.argv[1], 'rU')
output = open(sys.argv[2], 'w')

for records in SeqIO.parse(f, 'fastq'):
	records.id = records.id.split(' ')[0]
	records.description = records.description.split(' ')[0]
	SeqIO.write(records, output, "fastq")	
