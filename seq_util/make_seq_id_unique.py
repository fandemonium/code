import sys
import re

id = []
seq = []

for line in open(sys.argv[1], 'rU'):
	line = line.strip()
	if line.startswith(">"):
		lexemes = re.split(">|  |,", line)
		gi = lexemes[1]
		loc = re.split("=|[..]", lexemes[2])[1]
		newloc = loc.replace("(", "_")
		newid = gi + "_"+newloc
		id.append(newid)
	else:
		seq.append(line)

na = dict(zip(id, seq))
fa_out = open(sys.argv[2], 'w')
for item in na:
	fa_out.write(">gi%s\n" % item)
	fa_out.write("%s\n" % na[item])	
