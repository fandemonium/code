import os.path
## This script creates one folder for each genome, downloads only the files related to genomic nucleotide sequence.
## The input genome list file can be retrieved by the following command:
## wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt

import sys
from ftplib import FTP 
import os
ftp = FTP('ftp.ncbi.nlm.nih.gov','anonymous','dooley.shanek@gmail.com')

genomeList = open(sys.argv[1],'r')
errFile = open(sys.argv[2],'w')
genomeList.next()

for line in genomeList:
    lineArr = line.strip().split("\t")
    folderName = lineArr[1]
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    if "ftp" in lineArr[-1]:
        ftpFolder = lineArr[-1].replace("ftp://ftp.ncbi.nlm.nih.gov","")
    else:
        continue
    ftp.cwd(ftpFolder)
    filenames = ftp.nlst()
    for filename in filenames:
        if "genomic.fna" in filename:# or "report.txt" in filename or "stats.txt" in filename:
            try:
                if not os.path.exists(folderName+"/"+filename):
                    ftp.retrbinary('RETR ' + filename, open(folderName+"/"+filename,'wb').write)
                    print "Downloaded",folderName+"/"+filename
            except Exception as e:
                errFile.write(folderName + ": genomic file not found, python err: " + str(e) + "\n")
                    
ftp.quit()
