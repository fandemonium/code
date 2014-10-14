import sys
from ast import literal_eval

u = []
l = []
for line in open(sys.argv[1]):
    line = line.strip()
    lexemes = line.split('\t')
    ids = lexemes[-1].partition('accession')
    #print ids
    acc = ids[-1].rsplit(' ')
    l.append(acc[-1])
print len(l)
for x in l:
    if x not in u:
        u.append(x)
print len(u)
