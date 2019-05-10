import sys 
from Bio import SeqIO
import re

def get_singles(derep_seqs):
    l = []
    for record in SeqIO.parse(derep_seqs, 'fasta'):
        size = int(re.split(";|=", record.id.strip())[-2])
        if size == 1:
		l.append(record)
    return l

out_fa = sys.argv[1]
derep_seqs = sys.argv[2:]

for f in derep_seqs:
	singles = get_singles(f)
SeqIO.write(singles, out_fa, "fasta")

