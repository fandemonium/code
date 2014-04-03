import sys
import os

##~/Documents/Fan/scratch/parsed_files/combined$ for i in *.combined; do python ~/Documents/Fan/code/combine_taxa.py ~/Documents/Databases/uniprotKB_id_prok.txt $i > ~/Documents/Fan/scratch/parsed_files/kingdom_combined_no_restriction/$i.kingdom; done 

dict = {}
for line in open(sys.argv[1]):
       line = line.rstrip()
       lexeme = line.split("\t")
       id = lexeme[0]
       tax = lexeme[1]
       dict[id] = [tax]
       #print dict[id][0]
for line in open(sys.argv[2]):
        line = line.rstrip()
        data = line.split("\t")
        uni = data[1]
        uid = uni.split("|")[1]
        if uid in dict.keys():
		data.append(dict[uid][0])
		print '\t'.join(data)
