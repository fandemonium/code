import os
import sys
import gzip
from Bio import SeqIO

file_name = sys.argv[1]
if ".gz" in file_name:
	f = gzip.open(file_name)
else:
	f = open(file_name, 'rU')

new_file_name = "_".join(file_name.strip().split("/"))
out_name = new_file_name.split(".")[0] + ".fa"

pw = sys.argv[2]
out_path = pw + "/" + out_name

out = open(out_path, 'w')
for records in SeqIO.parse(f, "fastq"):
	records.id = new_file_name + ":" + records.id.strip()
#	print records.id
	SeqIO.write(records, out, 'fasta')
