import sys
import re
from Bio import Entrez

Entrez.email = "fyang@iastate.edu"

for lines in open(sys.argv[1],'rU'):
	
handle = Entrez.esearch(db="genome', term=
