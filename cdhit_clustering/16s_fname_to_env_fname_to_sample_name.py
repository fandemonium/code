import sys
import re

for lines in open(sys.argv[1], 'rU'):
	line = lines.strip()
	lexeme = re.split("_|-|\.", line)
	SAMPLE = "S_" + lexeme[2]
	ID_Miseq_ID = lexeme[0] + '-16s-' + lexeme[2].zfill(3)
	print '%s\t%s' % (ID_Miseq_ID, SAMPLE)
