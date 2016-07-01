import sys
from Bio import SeqIO

def seq_range(s_start, s_end):
	return str(s_start) + "-" + str(s_end) if s_end - s_start > 0 else str(s_end) + "-" + str(s_start)

def parse_seqid(fasta):
	seq_d = {}
	for records in fasta:
		header = records.id.strip().split(" ")
		ID = header[0]	
		seq_d[ID] = records.seq
	return seq_d

d = {}
for n, lines in enumerate(open(sys.argv[1], 'rU')):
	if n == 0:
		continue
	else:
		line = lines.strip().split("\t")
		seq_id = line[1]
		identity = float(line[2])
		type = line[-3]
		start = int(line[-7])
		end = int(line[-6])
		if identity >= 80:
			if type not in d:
				d[type] = [seq_id + ":" + seq_range(start, end)]
			else:
				d[type].append(seq_id + ":" + seq_range(start, end))
	
seqs = SeqIO.parse(open(sys.argv[2], 'rU'), "fasta")
fa = parse_seqid(seqs)
#for keys in fa.keys():
#	print keys

for args, values in d.iteritems():
#	print args
#	for item in values and fa.keys():
#			print ">" + item + "\n" + fa[item]
	fileout = "%s.txt" % args
	fp = open(fileout, 'w')
	for item in values:
		if item in fa.keys():
			fp.write(">%s\n" % (item))
			fp.write("%s\n" % (fa[item]))
