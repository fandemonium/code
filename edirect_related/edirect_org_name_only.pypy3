import sys

f = open(sys.argv[1], 'rU')
for lines in f.readlines()[1:]:
	line = lines.strip()#.split("\t")
	genus = line.split(" ")[0]
	species = line.split(" ")[1]
	print("esearch -db assembly -query \'%s\' | elink -target nuccore | elink -target assembly | efetch -format docsum | xtract -pattern DocumentSummary -element FtpPath_GenBank |awk -F\"/\" \'{print $0\"/\"$NF\"_rna_from_genomic.fna.gz\"}\' | xargs wget -O %s.rna.fa.gz" % (line, genus + "_" + species))
	#print "esearch -db assembly -query \'%s\' | elink -target nuccore | elink -target assembly | efetch -format docsum | xtract -pattern DocumentSummary -element FtpPath_RefSeq |awk -F\"/\" \'{print $0\"/\"$NF\"_rna_from_genomic.fna.gz\"}\' | xargs wget -O %s.rna.fa.gz" % (line, genus + "_" + species)

