from Bio import Entrez
import sys

l = []
for line in open (sys.argv[1]):
    lexemes = line.split('\t')
    #print len(lexemes)
    id = lexemes[-1]
    l.append(id.rstrip())
print l

for each in l:
    Entrez.email = "fyang@iastate.edu"
    handle = Entrez.efetch(db="nucleotide", id=each, rettype="gb", retmode="text")
    fp = open(each + '.full.gbk', 'w')
    fp.write('%s' % handle.read())
