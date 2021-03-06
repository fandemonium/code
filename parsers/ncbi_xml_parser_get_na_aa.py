import sys
import os
import re

f = sys.argv[1]
delimiters = [" ", "[", "]", "(", ")", ",", ";", ":", "."]

def rename(name):
	for ch in delimiters:
		if ch in name:
			name = name.replace(ch, "_")
	return name

title = []
na_seq = []
aa_seq = []
for line in open(f, 'rU'):
	line = line.strip()
	if line.startswith("<Seqdesc_title>"):
		ID = re.split(">|<", line)[2]
#		print ID
#		print rename(ID)
		title.append(rename(ID))
	if line.startswith("<IUPACna>"):
		na = re.split(">|<", line)[2]
		na_seq.append(na)
	if line.startswith("<IUPACaa>"):
		aa = re.split(">|<", line)[2]
		aa_seq.append(aa)
	
d_na = dict(list(zip(title, na_seq)))
d_aa = dict(list(zip(title, aa_seq)))

na_out = "%s.na.fa" % f.split(".")[0]
na_f = open(na_out, 'w')
for na_key in d_na:
	if "lactamase" in na_key:
#		print na_key
		if len(d_na[na_key]) >= 900 and len(d_na[na_key]) <= 1500:
#		if len(d_na[na_key]) >= 900:
			na_f.write('>%s_%s\n' % (f.split(".")[0], na_key))
			na_f.write('%s\n' % d_na[na_key])

aa_out = "%s.aa.fa" % f.split(".")[0]
aa_f = open(aa_out, 'w')
l = []
for aa_key in d_aa:
	if "lactamase" in aa_key:
#		print aa_key
		if len(d_aa[aa_key]) >= 300 and len(d_aa[aa_key]) <= 500:
			aa_f.write('>%s_%s\n' % (f.split(".")[0], aa_key))
			aa_f.write('%s\n' % d_aa[aa_key])

	
	
