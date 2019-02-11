import sys
import re

for lines in open(sys.argv[1], "rU"):
    line = lines.strip()
    lexemes = re.split(".out:", line)  
    oid = lexemes[0].split(".")[1]
    ncbi = re.split("val=|'", lexemes[1])[2]
    print(oid + " \t" + ncbi)
