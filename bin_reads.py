##########################################################################################
## to use in binning pandakiller assembled samples into seqfilter parsed tag directories############################################################################################
import os
import sys
from Bio import SeqIO
import string

assemb = open(sys.argv[1], 'rU')
dict_assemb = SeqIO.to_dict(SeqIO.parse(assemb, "fastq"))
for ID in dict_assemb:
	ID_new = ID.rsplit(':', 1)[0]
	dict_assemb[ID_new] = dict_assemb.pop(ID)
#print len(dict_assemb)
rootdir = "."
lfiles = []
for topdir, subdir, filelist in os.walk(rootdir):
	for files in filelist:
		if files.endswith("trimmed.fasta"):
			lfiles.append(files)

for each in lfiles:
	fout = '%s_assem.fastq' % each.strip()
        fp = open(fout, 'w')
	f = open(each, 'rU')
	l = []
	for records in SeqIO.parse(f, 'fasta'):
		name = records.id.split(' ')[0]
		if name in dict_assemb:
			#print each + ':' + name
			l.append(name)
#	print len(l)
	for item in l:
		SeqIO.write(dict_assemb, fp, 'fastq')
#		fp.write('>%s\n' % item) 
#		fp.write('%s\n' % dict_assemb[item])
#	for files in filelist:
#		if files.endswith("trimmed.fasta"):
#			lfiles.append(files)
#			for each in lfiles:
#				outfiles_keep = open(each + '_' + 'assem' + '.fasta', 'w')
				#outfiles_drop = open(each + '_' + 'dropped' + 'reads' + '.txt', 'w')
#				f = open(each, 'rU')
#				names = []
#				for records in SeqIO.parse(f, 'fasta'):
#					names.append(records.id.split(' ')[0])
#				for item in names:
#					if item in dict_assemb:	
#						outfiles_keep.write('>%s\n' % (item))
#						outfiles_keep.write('%s\n' % (dict_assemb[item]))
					#else:
					#	outfiles_drop. write('%s\n' % (item))
