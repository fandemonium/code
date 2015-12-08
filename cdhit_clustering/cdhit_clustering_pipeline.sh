cd 1_rdp_demultiplex/fastas

#renameing sequences
for i in *.fa; do python /mnt/data3/fan/code/cdhit_clustering/renaming_seq_w_short_sample_name.py $i ../../3_cdhit_otus/renamed_seqs/"$i".renamed.fa; done

#concatenate everything
cd ../../3_cdhit_otus/renamed_seqs/
cat *.fa > ../combined_renamed_seqs.fa

#clustering
cdhit-est -i combined_renamed_seqs.fa -o combined_renamed_seqs_cdhit.fasta -c 0.97 -M 8000 -T 3

#make otu table
python /mnt/data3/fan/code/cdhit_clustering/rep_seq_to_otu_mapping.py combined_renamed_seqs_cdhit.fasta.clstr > combined_renamed_seqs_cdhit_rep_seq_to_cluster.map

#convert otu table to wide format (otus as rows, samples as columns)
sudo Rscript /mnt/data3/fan/code/cdhit_clustering/convert_otu_table_long_to_wide_format.R cdhit_otu_table_long.txt cdhit_otu_table_wide.txt

#map otus to repseqs for rdp classified filterbyconf taxa table
sudo Rscript /mnt/data3/fan/code/cdhit_clustering/renaming_taxa_rep_seq_to_otus.R cdhit_otu_taxa_filterbyconf.txt combined_renamed_seqs_cdhit_rep_seq_to_cluster.map ../R/cdhit_taxa_table_w_repseq.txt

#env file from Angela kent need to be mapped to the otu and taxa
##1. create the mapping file
python /mnt/data3/fan/code/cdhit_clustering/16s_fname_to_env_fname_to_sample_name.py all_16s_sample_names.txt > 16s_sample_name_to_env_table.map
##2. merging in R

