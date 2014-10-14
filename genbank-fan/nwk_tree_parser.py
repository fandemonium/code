import sys 
from Bio import Phylo

names = {}
tree = Phylo.read(sys.argv[1], "newick")

for idx, clade in enumerate(tree.find_clades()):
    
    if clade.name:
        clade.name = '%d\t%s' % (idx, clade.name)
        print clade.name
   # else:
    #    clade.name = str(idx)
    #    names = clade.name
    #    print names

