import sys
import re

for lines in open(sys.argv[1], 'rU'):
	if lines.startswith("#"):
		continue
	else:
		line = lines.strip().split()
		arg_name = line[0]
		arg_acc = line[1]
		mock_id = line[2]
		e_value = line[4]
		score = line[5]
		bias = line[6]
		aro = line[-1]
		print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (mock_id, arg_name, arg_acc, e_value, score, bias, aro)

