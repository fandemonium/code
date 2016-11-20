#input data:
#```
#NZ_AFRW01000000.gbk:WGS         AFRW01000001-AFRW01000138
#NZ_AFUK01000000.gbk:WGS         AFUK01000001
#NZ_AFUR01000000.gbk:WGS         AFUR01000001-AFUR01000007
#```

import os
import sys
from Bio import Entrez

for lines in open(sys.argv[1], 'rU'):
	line = lines.strip().split()
	ncbi_org_acc = line[0].split(".")[0]
	if not os.path.exists(ncbi_org_acc):
		os.mkdir(ncbi_org_acc)
	if "-" in line[1]:
		contig_acc_range = line[1].split("-")
		start =  int(contig_acc_range[0][-2:])
		end = int(contig_acc_range[-1][-2:])
		l = range(start,end+1)
		prefix = contig_acc_range[0][:-2]
	else:
		contig = line[1].strip()
		l = [int(contig[-2:])]
		prefix = contig[:-2]
	f = open(ncbi_org_acc + '/' + ncbi_org_acc + '.contigs.txt', 'w')
	for seqs in l:
		contigs = prefix + "%02d" % seqs
		f.write('%s\n' % contigs)
