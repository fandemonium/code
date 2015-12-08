cut -f 2 uparse_otu_table_97.txt | sed "1d" | paste -sd+ - | bc
