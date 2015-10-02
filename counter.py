#parse id, find unique id and count how many times it showed up, then add the file name to it#
#usage: for i in *.tips.txt; do python ~/Documents/repos/code/counter.py $i; done > clade_trait_table.txt 

import sys
import os
from collections import Counter

tip = sys.argv[1]
IDs= Counter()
for line in open(tip, 'rU'):
	line = line.strip().split("|")
	oid = line[0]
	IDs[oid] += 1

for keys in IDs:
	print "%s\t%s\t%s" %(keys, IDs[keys], tip.split(".")[0])
