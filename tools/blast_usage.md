# make blast db into specific directory with a specific name (-out)
```
makeblastdb -in strain_16s.fa -parse_seqids -dbtype nucl -out n_soi_db/n_soi
```

# best hit 1 results
```
blastn -db n_soi_db/n_soi -query ../3_cdhit_clustering/renamed_seqs/all_renamed_sequences.fa -evalue 1e-5 -max_target_seqs 1 -out n_soi.blast -num_threads 8 -outfmt "6 qseqid sseqid pident qlen length evalue bitscore"
```
