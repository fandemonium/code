#! /usr/bin/env python

#Parser for blast -m 8 or blast+ -m 6 and 7 output file with description inserted

import sys

##Query id,Subject id,Description, % identity, alignment length,mismatches,gap openings,q. start,q. end,s. start,s. end,e-value,bit score
dict1={}
for line in open(sys.argv[1]):
        data = line.split('\t')
#       print(data)
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
        if e_value > 1e-5:
                if query in dict1:
                        dict1[query].append([hit, hit_desc, identity, length, q_start, q_end, e_value, bit_score])
                else:
                        dict1[query] = [[hit, hit_desc, identity, length, q_start, q_end, e_value, bit_score]]
		print('%s\t%s\t%s' % (query, dict1[query][0][3], dict1[query][0][-2]))
