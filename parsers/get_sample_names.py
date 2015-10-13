import sys
import re

for lines in open(sys.argv[1], 'rU'):
	line = lines.strip()
	lexemes = re.split("/|\.", line)
	names = lexemes[2].split("_")
	#print len(names)
	if len(names) == 7 and names[-2] == "R1":
		otu_name = lexemes[0] + '_' + names[3] + '_assembled'
		sample_name =  names[0] + '_' + names[1] + '_' + names[2]
		print "%s\t%s" %(otu_name, sample_name)
	elif len(names) == 5 and names[-2] == "R1":
		otu_name = lexemes[0] + '_' + names[-4] + '_assembled'
                sample_name =  names[0].split('-')[0] + '_' + names[0].split('-')[1] + '_' + names[0].split('-')[2] 
		print "%s\t%s" %(otu_name, sample_name)
