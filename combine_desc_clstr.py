#!/usr/bin/python

##input 1: anything resembles /Users/metagenomics/Documents/Fan/scratch/parsed_files/clstr_parsed/x701_Asp.clstr.parsed
##input 2: anythong resembles /Users/metagenomics/Documents/Fan/scratch/parsed_files/blast_parsed/x701_Asp_nucl_cdhit.blast.desc.parsed

#########
## see combine_clstr_labst_wrap.sh
###

import sys
import os
import re

con_info = {}
for line in open(sys.argv[1]):
	line = line.rstrip()
	lexeme = line.split("\t")
	clstr = lexeme[0]
	contig = lexeme[1]
	abun = lexeme[-1]
	x = contig.split('_')[0] + "_" + contig.split('_')[1]
	con_info[x] = [clstr, abun]
#print con_info[x][0]

for bline in open(sys.argv[2]):
        bline = bline.rstrip()
        data = bline.split("\t")
	bcontig = data[0]
	id = data[1]
	a = id.split('|')[1]
	b = id.split('|')[2]
        y = bcontig.split('_')[0] + "_" + bcontig.split('_')[1]
	if y in con_info.keys():
		data.append(con_info[y][0])
		data.append(con_info[y][1])
		print '\t'.join(data)
	#print data       


