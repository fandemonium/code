import sys

f = sys.argv[2]

for lines in open(sys.argv[1], 'rU'):
	pair = lines.strip().split("\t")
	fwd = pair[0]
	rev = pair[1]
	print "grep -o -P '(" + fwd + ").*(" + rev + ")' " + f + " > " + "p450_" + f.rsplit(".", 1)[0] + "_" + fwd + "_" + rev + ".fa"
#	print "grep -o -P '(?<=" + fwd + ").*(?=" + rev + ")' " + f + " > " + "p450_" + f.rsplit(".", 1)[0] + "_" + fwd + "_" + rev + ".fa"

