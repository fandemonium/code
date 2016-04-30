import sys

d = {}
for lines in open(sys.argv[1], 'rU'):
	lexemes = lines.strip().split("\t")
	if len(lexemes) in d:
		d[key] += 1
		d[key] = lines
	else:
		d[key] = 1
		d[key].append(lines)	
print d
#	if len(lexemes) not in l:
#		l.append(len(lexemes))
#		
#for item in l:
#	outfile = "ncol.%s.txt" % (item)
#	if len(lexemes) == item:
#		outfile.write(lines)

