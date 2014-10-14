from Bio import Entrez
import sys

l = []
for line in open (sys.argv[1]):
#    lexemes = line.strip()
#    lexemes = line.partition('accession ')
    id = line.strip()
    l.append(id.rstrip('\n\t'))
print l

for each in l:
    Entrez.email = "fyang@iastate.edu"
    handle = Entrez.efetch(db="nucleotide", id=each, rettype="gb", retmode="text")
    fp = open(each + '.dbsource.gbk', 'w')
    fp.write('%s' % handle.read())
