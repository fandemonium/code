import sys

f = open(sys.argv[1], 'rU')
for lines in f.readlines()[1:]:
	lexeme = lines.strip().split("\t")
	oid = lexeme[0]
	org = lexeme[1]
	print "esearch -db assembly -query \'\"%s\"[Organism]\' | elink -target nuccore | elink -target assembly | efetch -format docsum | xtract -pattern DocumentSummary -element FtpPath_GenBank |awk -F\"/\" \'{print $0\"/\"$NF\"_rna_from_genomic.fna.gz\"}\' | xargs wget -O %s.rna.fa.gz" % (org, oid)

