#! /usr/bin/env python

#Parser for blast -m 8 or blast+ -m 6 and 7 output file with description inserted

import sys

##Query id,Subject id,Description, % identity, alignment length,mismatches,gap openings,q. start,q. end,s. start,s. end,e-value,bit score
dict1={}
for line in open(sys.argv[1]):
	data = line.strip().split('\t')
	query = data[0]
	hit = data[1]
	identity = float(data[2])
	aln_len = int(data[3])
	q_start = int(data[6])
	q_end = int(data[7])
	e_value = float(data[-2])
	bit_score = float(data[-1])
	if e_value <= 1e-5:
		if query in dict1:
			dict1[query].append([hit, hit_desc, identity, length, q_start, q_end, e_value, bit_score])
		else:
			dict1[query] = [[hit, hit_desc, identity, length, q_start, q_end, e_value, bit_score]]	
#print len(dict1)

dict2={}
for key in list(dict1.keys()):
		if len(dict1[key]) > 1:
			dict2[key] = dict1[key][0]
		else:
			dict2[key] = dict1[key][0]
#print dict2

output = open(sys.argv[2], 'w')
for key in list(dict2.keys()):
	output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (key, dict2[key][0], dict2[key][1], dict2[key][2], dict2[key][3], dict2[key][-2], dict2[key][-1]))
