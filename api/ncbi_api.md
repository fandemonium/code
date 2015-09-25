# create a list of id #
```
$ less euk_ncbi_id.txt 
AX059457
AB278124
EU884135
M60302
```

# use curl or wget to get genbank files (rettype=gb) or fastas (rettype=fasta) #
while read id; do curl "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id="$id"&rettype=gb&retmode=text" > "$id".gb; done < euk_ncbi_id.txt
