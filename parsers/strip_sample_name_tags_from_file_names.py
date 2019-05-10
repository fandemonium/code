import sys
import os
import re

l = []
for lines in open(sys.argv[1], 'rU'):
        lexeme = lines.strip().split("_")
        name = '_'.join(lexeme[:-2])
#        print tag 
	if name not in l:
		l.append(name)
print('\n'.join(l))

