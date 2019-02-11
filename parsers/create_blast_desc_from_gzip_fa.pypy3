#!/usr/bin/python

import sys
import gzip

if len(sys.argv) != 3:
    print("USAGE:  create-desc.py <db file> <out file>")
    sys.exit(1)

fp = open(sys.argv[2], 'w')
for line in gzip.open(sys.argv[1]):
    if line.startswith('>'):
        line = line[1:]
        fp.write(line)
        
