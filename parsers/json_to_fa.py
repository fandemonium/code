import json
import sys
import argparse
import re

parser = argparse.ArgumentParser(description='Parse json files with different keys')
parser.add_argument('infile', metavar='json', type=argparse.FileType('r'), nargs='+', help='1+ json file as the input')
parser.add_argument('--source', metavar='type1|type2', help="Tag for where the json files were pulled from, type1 represents source 1, and type2 represents source 2")

args = parser.parse_args()

def type1_parser(JSON):
	type1_id = JSON.split(".")[0]
	parsed = json.load(open(JSON))
	seqs = parsed["sequence16s"]["text"].strip('N')
	return ">" + type1_id + "\n" + seqs

def type2_parser(JSON):
	parsed =json.load(open(JSON))
	d = {}
	try:
		for items in parsed:
			seq_id = items["isolate_id"]
			seqs = items["fasta"].strip('N')
			if items["taxonomy"] is None:
				taxa = "strains"
			else:
				taxa = items["taxonomy"]
			type2_id = seq_id + ":" + taxa
			if type2_id not in d:
				d[type2_id] = [seqs]
			else:
				d[type2_id].append(seqs)
		return d
	except:
		pass

if args.source == 'type1':
	for f in args.infile:
		print(type1_parser(f.name))
elif args.source == 'type2':
	for f in args.infile:
		isolates = type2_parser(f.name)
		try:
			for key, value in isolates.items():
				for i in range(0, len(isolates[key])):
					print(">" + key + ":" + str(i) + "\n" + isolates[key][i])
		except:
			pass
else:
	print(parser.print_help())
