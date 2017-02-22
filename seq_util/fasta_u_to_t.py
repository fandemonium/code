import sys
from Bio import SeqIO
import gzip

f = gzip.open(sys.argv[1], 'r') 

for records in SeqIO.parse(f, 'fasta'):
	dna = str(records.seq).replace("U", "T")
	print "%s%s\n%s" %(">", records.id, dna) 
	#SeqIO.write(records, out , "fasta")
