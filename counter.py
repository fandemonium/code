import sys
import os

#def count_id(ids):
tip = sys.argv[1]
n = 1
IDs={}
for line in open(tip, 'rU'):
	line = line.strip().split("|")
	oid = line[0]
	if oid not in IDs:
		IDs[oid] = [n, tip.split(".")[0]]
	else:
		IDs[oid] = [n+1, tip.split(".")[0]]

for keys in IDs:
	print "%s\t%s\t%s" %(keys, IDs[keys][0], IDs[keys][1])
