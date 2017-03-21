import sys
from Bio import SeqIO
import gzip
import operator
import re

## usage:
## python pull_16s_from_ncbi.rna.fa.gz_files.py <genes_to_extract> <minimal_sequence_length> <file_id_without_genes.error> file1 file2 file3 ...
## python ~/repos/code/seq_util/pull_16s_from_ncbi.rna.fa.gz_files.py "16S|SSU|ssu" 500 test.error *.rna.fa.gz 
## the final output returns the longest 16S gene identified for each input ncbi.rna.fa.gz file. File name is written into the sequence header. 

def keyword_l(GENES):
	if "|" in GENES:
		keyword_list = GENES.split("|")
	else:
		keyword_list = GENES
	return keyword_list
	
def ext_genes(fasta, KEYWORDS, LEN):
	d = {}
	for records in SeqIO.parse(fasta, "fasta"):
		kl = keyword_l(KEYWORDS)
		if any(kw in records.description for kw in kl) and len(records.seq) >= int(LEN):
#			print ">" + img_oid + "::" + records.id + "::" + records.description + "\n" + records.seq
			d[records.id] = [records.id, records.description, records.seq]
	return d

no_genes_out = open(sys.argv[3], 'w')
l = []	
for f in sys.argv[4:]:
	img_oid = f.strip().split(".")[0]
	unzip_f = gzip.open(f)
	gene_records = ext_genes(unzip_f, sys.argv[1], sys.argv[2])
	if len(gene_records) > 0:
		longest_seq_key = max(gene_records.iteritems(), key=operator.itemgetter(1))[0]
		print ">"+ img_oid +"::" + longest_seq_key + "::" + gene_records[longest_seq_key][1] + "\n" +gene_records[longest_seq_key][-1]
	else:
		l.append(img_oid)
no_genes_out.write("\n".join(l))
