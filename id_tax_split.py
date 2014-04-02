import os
import sys

for line in open(sys.argv[1]):
	line = line.strip()
	lexeme = line.split("\t")
	id = lexeme[0]
	print id
