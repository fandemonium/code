import sys 
from Bio import SeqIO

file = open(sys.argv[1], 'rU')
#for records in SeqIO.parse(file, 'genbank'):
#    print records
fa = SeqIO.convert(file, "genbank", open(sys.argv[2], 'w'), "fasta")
