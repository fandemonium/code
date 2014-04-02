#! /usr/bin/env python

#Parser for blast -m 8 output file with description inserted

import sys

##Query id,Subject id,Description, % identity, alignment length,mismatches,gap openings,q. start,q. end,s. start,s. end,e-value,bit score
dict={}
for line in open(sys.argv[1]):
	data = line.split('\t')
#	print(data)
	query = data[0]
	hit = data[1]
	hit_desc = data[2]
	identity = float(data[3])
	length = int(data[4])
	q_start = int(data[7])
	q_end = int(data[8])
	e_value = float(data[-2])
	if "hydrogenase" in hit_desc and e_value <= 1e-5:
		if dict.has_key(query):
			dict[query].append([hit, hit_desc, identity, length, q_start, q_end, e_value])
		else:
			dict[query] = [[hit, hit_desc, identity, length, q_start, q_end, e_value]]		
#print dict
dict2={}
for key in dict.keys():
	if len(dict[key]) > 1:
		if dict[key][0][-1] <= dict[key][1][-1]:
			dict2[key] = dict[key][0]
		else: 
			dict2[key] = dict[key][1]
	else:
		continue
#print dict2

output = open(sys.argv[2], 'w')
for key in dict2.keys():
	output.write('%s\t%s\t%s\t%s\t%s\n' % (key, dict2[key][1], dict2[key][2], dict2[key][3], dict2[key][-1]))
