# best hit 50 results
```
blastn -db ../../databases/rdp_16s_derep/rdp_16s_derep -query ../3_cdhit_clustering/master_otus/relabeled_denovo_ref_good_cdhit_97 -evalue 1e-5 -max_target_seqs 50 -out rdp_16s_derep.blast -num_threads 8 -outfmt 6
```
