import json
import sys

f = open(sys.argv[1], 'rU')

d = {}
for n, info in enumerate(json.load(f)):
	d[n] = [info]

# add table header
for lexemes in d.values()[0]:
	print '\t'.join(lexemes.keys())
# table contents
for keys, values in d.items():
	for items in values:
		print '\t'.join(str(x) for x in items.values())
