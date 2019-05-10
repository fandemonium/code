# make blast db into specific directory with a specific name (-out)
```
makeblastdb -in strain_16s.fa -parse_seqids -dbtype nucl -out n_soi_db/n_soi
```

# best hit 1 results
```
blastn -db n_soi_db/n_soi -query ../3_cdhit_clustering/renamed_seqs/all_renamed_sequences.fa -evalue 1e-5 -max_target_seqs 1 -out n_soi.blast -num_threads 8 -outfmt "6 qseqid qstart qend qlen sseqid sstart send length pident evalue bitscore"
```

# get blast seq headers/descriptions directly from blast db. 
```
mkdir /A/DIR/TO/COLLECT/ALL/TITLE/FILES/
while read line; do echo "blastdbcmd -db /PATH/TO/DB/DB_NAME -entry "\"$line\"" -outfmt %t > /A/DIR/TO/COLLECT/ALL/TITLE/FILES/${line//|/_}.title"; done > get_title.sh
cat get_title.sh | parallel
# once finished running:
paste -d "\t" <(grep "" *.title | cut -d ":" -f 1 | rev | cut -d "." -f 2- | rev) <(grep "" *.title | cut -d ":" -f 2) > ../combined_titles.txt
```
