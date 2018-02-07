import json
import sys

f = open(sys.argv[1], 'rU')

for items in json.load(f):
	for keys in items:
		print keys + '\t' + str(items[keys])

