import sys
from Bio import SeqIO

# example:
# python $efs/repos/code/seq_util/seqfilter_add_droppedseqs.py NoTag_dropped_seqs.txt NoTag_trimmed.fastq $efs/inflated_otus/SEQ26610/trimmed_q25/1_forward_trim/MiSeq_2187_1_N719-S515_1.q25.fq | less

# from rdp SeqFilter output
dropped = open(sys.argv[1], 'rU') #NoTag_dropped_seqs.txt
trimmed = SeqIO.parse(open(sys.argv[2]), 'fastq') #NoTag_trimmed.fastq
seqs = SeqIO.parse(open(sys.argv[3]), 'fastq') #previous sequences used as input for SeqFilter

to_add = []
for lines in dropped.readlines()[1:]:
	line = lines.strip().split('\t')
	if line[1] == "Primer trimmer" and "best partial match" not in line[2]:
		to_add.append(line[0])

for good in trimmed:
	print good.format("fastq").strip()

for records in seqs:
	if records.id in to_add:
#		print records.id
		print records.format("fastq").strip()
