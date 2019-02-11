import sys
import os

## input 1: /Users/metagenomics/Documents/Databases/uniprotKB_id_prok.txt
## input 2: anything resembles /Users/metagenomics/Documents/Fan/scratch/parsed_files/combined/x701_Asp.combined

##~/Documents/Fan/scratch/parsed_files/combined$ for i in *.combined; do python ~/Documents/Fan/scratch/code/combine_taxa.py ~/Documents/Databases/uniprotKB_id_prok.txt $i > ~/Documents/Fan/scratch/parsed_files/kingdom_combined/$i.kingdom; done

dic = {}
for line in open(sys.argv[1]):
       line = line.rstrip()
       lexeme = line.split("\t")
       ID = lexeme[0]
       tax = lexeme[1]
       dic[ID] = [tax]
       #print ID + dic[ID][0]
for line in open(sys.argv[2]):
        line = line.rstrip()
	data = line.split("\t")
        uni = data[2]
	uid = uni.split("|")[1]
        if uid in list(dic.keys()):
		data.append(dic[uid][0])
		print('\t'.join(data))
