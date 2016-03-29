## in case of a large file, this scripts performs split without read everything into RAM
import sys
import os

#if len(sys.argv) != 3:
#	sys.exit("USAGE: split_1_file_into_multiple_by_pattern.py <path_to_save_files> <split_pattern> <input.txt>")

# define writing file function:
def files():
	n = 0
	while True:
		n += 1
#		for line in whole_file:
#			if line.startswith("ACC"):
#				name = line.strip().split("\t")[1]
		yield open(sys.argv[1] + '/%s.hmm' % str(n), 'w')

pattern = sys.argv[2]
fs = files()
outfile = next(fs)

with open(sys.argv[3]) as infile:
	for line in infile:
		if pattern not in line:
			outfile.write(line)
		else:
			items = line.split(pattern)
			outfile.write(items[0])
			for item in items[1:]:
				outfile = next(fs)
				outfile.write(pattern + item)

