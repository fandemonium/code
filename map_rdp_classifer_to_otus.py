import os
import sys

d_otu = {}
for lines in open(sys.argv[1], 'rU'):
	lines = lines.strip()
	data = lines.split('\t')
	otu = data[0]
	domain = data[2]
	d_sc = data[4]
	phylum = data[5]
	p_sc = data[7]
	cla = data[8]
	c_sc = data[10]
	order = data[11]
	o_sc = data[13]
	fam = data[14]
	f_sc = data[16]
	genus = data[17]
	g_sc = data[19]
	species = data[-3]
	s_sc = float(data[-1])
	try:
		if s_sc >= 0.5:
		print '%s;%s;%s;%s;%s;%s;%s' % (domain, phylum, cla, order, fam, genus, species)
