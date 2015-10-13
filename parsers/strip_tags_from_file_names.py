import sys
import os
import re

l = []
for lines in open(sys.argv[1], 'rU'):
        lexeme = lines.strip().split("_")
        tag = lexeme[-4]
        print tag 
	if tag not in l:
		l.append(tag)
print '\n'.join(l)

