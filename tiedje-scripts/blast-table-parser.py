#! /usr/bin/env python

"""
A parser for the -m 8 blast output
"""

import sys

if len(sys.argv) != 2:
    print "USAGE:  blast-table-parser.py <blat file>"
    sys.exit(1)

CONTIG_THRESHOLD = 1000
E_THRESHOLD = 1e-5
IDENTITY_THRESHOLD = 30

dict = {}

#Query id,Subject id,% identity,alignment length,mismatches,gap openings,q. start,q. end,s. start,s. end,e-value,bit score
for line in open(sys.argv[1]):
    data = line.split('\t')
    query = data[0]
    hit = data[1]
    identity = float(data[2])
    length = int(data[3])
    q_start = int(data[6])
    q_end = int(data[7])
    e_value = float(data[-2])
    
    contig_length = int(query.split('_')[3])+33-1

    '''only examining contigs > 1000 and with evalues > 1e-5'''

    if contig_length >= CONTIG_THRESHOLD and identity >= int(IDENTITY_THRESHOLD):
        print line.rstrip()

    
