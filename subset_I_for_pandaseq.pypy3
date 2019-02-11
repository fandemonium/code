## If you wnat to use RDP assembler or original pandaseq, use this script to subset your barcode file to have the exact sequence (same ID) that's in your sequence file. This script is used to subset FIXED_I.fastq to match with ASSEMBLE_READS.fastq (from RDP assembler). Qiime doesn't like if you have more sequences in your barcode file than your sequence file. 

import sys
import gzip
from Bio import SeqIO

if len(sys.argv) != 4:
	print("USAGE: python subset_I_for_pandaseq.py ASSEMBLED_READS.fastq FIXED_I.fastq SUBSET_FIXED_I.fastq")
	sys.exit()

l_id = []
assem = open(sys.argv[1], 'rU')
## if it's a fastq.gz file, uncomment the line below and hash the line above. 
#assem = gzip.open(sys.argv[1], 'rU')
for records in SeqIO.parse(assem, 'fastq'):
	l_id.append(records.id)
#print len(l_id)

tags = open(sys.argv[2], 'rU')
tag_dict = SeqIO.to_dict(SeqIO.parse(tags, "fastq"))
#print tag_dict

out = open(sys.argv[3], 'w')
for item in l_id:
	SeqIO.write(tag_dict[item], out, "fastq")
