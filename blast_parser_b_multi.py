#! /usr/bin/env python

#Parser for blast -m 8 or blast+ -m 6 and 7 output file with description inserted

import sys

##Query id,Subject id,Description, % identity, alignment length,mismatches,gap openings,q. start,q. end,s. start,s. end,e-value,bit score
dict1={}
for line in open(sys.argv[1]):
	data = line.split('\t')
#	print(data)
	query = data[0]
	hit = data[1]
	#print hit
	hit_desc = data[2]
	#print hit_desc
	identity = float(data[3])
	length = int(data[4])
	q_start = int(data[7])
	q_end = int(data[8])
	e_value = float(data[-2])
	bit_score = float(data[-1])
	if e_value <= 1e-5:
		if "uncultured" not in hit_desc:
			if dict1.has_key(query):
				dict1[query].append([hit, hit_desc, identity, length, q_start, q_end, e_value, bit_score])
			else:
				dict1[query] = [[hit, hit_desc, identity, length, q_start, q_end, e_value, bit_score]]	
#print len(dict1)

dict2={}
for key in dict1.keys():
		if len(dict1[key]) > 1:
			dict2[key] = dict1[key][0]
		else:
			dict2[key] = dict1[key][0]
#print dict2

output = open(sys.argv[2], 'w')
for key in dict2.keys():
	output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (key, dict2[key][0], dict2[key][1], dict2[key][2], dict2[key][3], dict2[key][-2], dict2[key][-1]))
