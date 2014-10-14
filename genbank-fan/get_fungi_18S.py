import sys 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
#import fileinput

#to run on multiple, run
#for x in *gbk; do python parse-genbank2.py $x > $x.16s.fa; done


n = 0
l = []
for record in list(SeqIO.parse(sys.argv[1], 'genbank')):
    print record
    print len(record)
    org = record.annotations["source"]
    for feat in genome.features:
        if feat.type == "rRNA":
            if '18S' in feat.qualifiers['product'][0]:#or '16S ribosomal' for strict match
                start = feat.location.start.position
                end = feat.location.end.position
                pos = [start, end]
                l.append(pos)
                print '>' + sys.argv[1].split('.')[0] + org + ' '+ '18S rRNA gene' + str(n)                
                  #      print '>' + sys.argv[1].split('.')[0] + ' 16S rRNA gene ' + str(n) 
                #print feat.extract(genome.seq)
                n =+ 1

