import sys
import os
import re

for lines in open(sys.argv[1], 'rU'):
	lines = lines.strip()
	ID = re.split('\|', lines)[1]
	print(ID)
