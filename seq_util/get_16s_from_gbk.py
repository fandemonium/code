from Bio import Entrez
import sys

l = [] 
lines = open(sys.argv[1]).read().splitlines()
for number, line in enumerate(lines):
	if "16S ribosomal RNA" in line:
	#	print 'found line. previous line is: %s' % lines[number-1]
		l.append(lines[number-1])
print l

from Bio import Entrez
import sys

l = []
with open (sys.argv[1]) as f:
    next(f)
    for line in f:
        lexemes = line.split('\t')
        id = lexemes[-6]
        l.append(id.rstrip())
print l

for each in l:
    Entrez.email = "fyang@iastate.edu"
    handle = Entrez.efetch(db="nucleotide", id=each, rettype="gb", retmode="text")
    fp = open(each + '.gbk', 'w')
    fp.write('%s' % handle.read())
