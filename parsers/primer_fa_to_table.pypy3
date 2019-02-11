## usage:python ~/Documents/repos/code/parsers/primer_fa_to_table.py all_es_arg_primers.fa > all_es_arg_primers_truseq_and_conventional_pcr.table

import sys
import re
from Bio import SeqIO

def revcomp(fh):
	output = "";
	for i in range(0, len(fh)):
		if (fh[i] == 'c' or fh[i] == 'C'):
			output += "G"
		if (fh[i] == 'g' or fh[i] == 'G'):
			output += "C"
		if (fh[i] == 't' or fh[i] == 'T'):
			output += "A"
		if (fh[i] == 'a' or fh[i] == 'A'):
			output += "T"
	return output[::-1]

def get_primer_sets(fa_header):
	primer_names = fa_header.strip().split("_")
	if len(primer_names) == 5:
		gene = primer_names[0]
		sets = primer_names[-3][:(len(primer_names[-3])-1)]
		f_r = primer_names[-3][-1:]
		return gene + "\t" + sets + "\t" + f_r
	else:
		gene = primer_names[0] + "_" + primer_names[1]
		sets = primer_names[-3][:(len(primer_names[-3])-1)]
		f_r = primer_names[-3][-1:]
		return gene + "\t" + sets + "\t" + f_r

for records in SeqIO.parse(open(sys.argv[1]), "fasta"):
	primer_sets = get_primer_sets(records.id)
	if primer_sets.split("\t")[-1] == "r":
		pcr_seq = revcomp(records.seq)
		print(primer_sets + "\t" + records.seq + "\t" + pcr_seq)
	else:
		print(primer_sets + "\t" + records.seq + "\t" + records.seq)
		
