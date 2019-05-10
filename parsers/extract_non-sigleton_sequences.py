import sys 
from Bio import SeqIO
import re

def get_nonsingles(derep_seqs):
    l = []
    for record in SeqIO.parse(derep_seqs, 'fasta'):
        size = int(re.split(";|=", record.description.strip())[-2])
        if size > 1:
		l.append(record)
    return l

out_fa = sys.argv[1]
derep_seqs = sys.argv[2:]

for f in derep_seqs:
	nonsingles = get_nonsingles(f)
SeqIO.write(nonsingles, out_fa, "fasta")

