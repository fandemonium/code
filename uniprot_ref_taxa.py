## assign kingdoms to reference sequences
import sys
import os
import re

dict = {}
for line in open(sys.argv[1]):
       line = line.rstrip()
       lexeme = line.split("\t")
       id = lexeme[0]
       tax = lexeme[1]
       dict[id] = [tax]
       #print dict[id][0]
for line in open(sys.argv[2]):
        line = line.strip()
        ref = re.split('>|/', line)
        ref_id = ref[1].split('_')[0]
        #print id
        if ref_id in dict.keys():
                ref.append(dict[ref_id][0])
                print '\t'.join(ref)
