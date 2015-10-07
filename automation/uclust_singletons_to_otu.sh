usearch -derep_fulllength all_singleton_seqs.fa -fastaout all_singleton_seqs.fa_derep.fa -sizeout

usearch -sortbysize all_singleton_seqs.fa_derep.fa -fastaout all_singleton_seqs.fa_derep.fa_sorted.fa -minsize 2

### usually all singletons are real singletons, even you pool them all together, they are still singletons...###
