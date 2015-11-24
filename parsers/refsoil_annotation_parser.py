import sys
import re
import os

files = sys.argv[1:]

def line_stats(bind_ss):
	l = []
	for lines in bind_ss:
		line = lines.strip().split('\t')
		l.append(len(line))
	return 'max line length: ' + str(max(l)), 'min line length: ' + str(min(l))

#print line_stats(open(f, 'rU'))
	
#l_ec = []
#l_tc = []

def get_ec(description):
	l_ec = []
	n = description.count('(EC')	
	if n == 0:
		l_ec = ["NA"]
	elif n >= 1:
		for i in range(1, n+1):
			ec = desc.split('(EC')[-i].replace(')', '')
			ec = re.split(" |,|_", ec)[-1].replace('-', '0')
			l_ec.append(ec)
	return l_ec

def get_tc(description):
	l_tc = []
	n = description.count('(TC')	
	if n == 0:
		l_tc = ["NA"]
	elif n >= 1:
		for i in range(1, n+1):
			tc = desc.split('(TC')[-i].replace(')', '')
			tc = re.split(" |,|_", tc)[-1].replace('-', '0')
			l_tc.append(tc)
	return l_tc
for f in files:
	for lines in open(f, 'rU'):
		line = lines.strip().split('\t')
		fig_id = line[2].split("|")[1]
		gene = line[0]
		desc = line[1]
		EC = get_ec(desc)
		TC = get_tc(desc)
		if len(line) == 5:
			T1 = line[3]
			T2 = line[4]
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (fig_id, gene, desc, EC, TC, T1, T2)	
		elif len(line) == 4:
			T1 = line[3]
			T2 = "NA"
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (fig_id, gene, desc, EC, TC, T1, T2)	
		elif len(line) == 3:
			T1 = "NA"
			T2 = "NA"
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (fig_id, gene, desc, EC, TC, T1, T2)	
#	if fig_id in d:
#		d(fig_id).append([gene, desc, ec, tc, T1, T2])
#	else:
#		d(fig_id) = [[gene, desc, ec, tc, T1, T2]]
#	print d
#print "ec: " + str(len(l_ec)), "tc: " + str(len(l_tc))

