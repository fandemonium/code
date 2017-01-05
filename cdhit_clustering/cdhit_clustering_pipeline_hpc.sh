DIR="/mnt/scratch/yangfan1/narasin"
CODE="/mnt/home/yangfan1/repos/code/cdhit_clustering"
RDPTOOLS="/mnt/research/rdp/public/RDPTools/"
#### continue from after chimera check and remapping sequences: for i in *.fasta; do /mnt/research/rdp/public/thirdParty/usearch8.1.1831_i86linux64 -usearch_global $i -db ../chimera_check/all_combined_q25_otu1_ref_good_otu2.fa -strand plus -id 0.985 -matched ../../3_cdhit_clustering/quality_seqs/"$i"_finalized.fa; done"

mkdir $DIR/3_cdhit_clustering
cd $DIR/3_cdhit_clustering
mkdir renamed_seqs master_otus R
#renameing sequences, writing out mapping files, and one sequence files
cd $DIR/2_quality_check/final_good_seqs
python $CODE/renaming_seq_w_short_sample_name.py $DIR/3_cdhit_clustering/renamed_seqs/sample_filename_map.txt $DIR/3_cdhit_clustering/renamed_seqs/sequence_name_map.txt > $DIR/3_cdhit_clustering/renamed_seqs/all_renamed_sequences.fa

#clustering
module load CDHIT/4.6.1
cd $DIR/3_cdhit_clustering/master_otus
cd-hit-est -i ../renamed_seqs/all_renamed_sequences.fa -o combined_renamed_seqs_cdhit.fasta -c 0.97 -M 8000 -T 3

#make otu table
python $CODE/cdhit_clstr_to_otu.py combined_renamed_seqs_cdhit.fasta.clstr > cdhit_otu_table_long.txt

#convert otu table to wide format (otus as rows, samples as columns)
module load R/2.15.1
Rscript $CODE/convert_otu_table_long_to_wide_format.R cdhit_otu_table_long.txt ../R/cdhit_otu_table_wide.txt

##identify otu taxonomy
module load Java/1.7.0_51
java -Xmx24g -jar $RDPTOOLS/classifier.jar classify -c 0.5 -f filterbyconf -o cdhit_otu_taxa_filterbyconf.txt -h cdhit_otu_taxa_filterbyconf_hierarchy.txt combined_renamed_seqs_cdhit.fasta

#map otus to repseqs for rdp classified filterbyconf taxa table
python $CODE/rep_seq_to_otu_mapping.py combined_renamed_seqs_cdhit.fasta.clstr > combined_renamed_seqs_cdhit_rep_seq_to_cluster.map
Rscript $CODE/renaming_taxa_rep_seq_to_otus.R cdhit_otu_taxa_filterbyconf.txt combined_renamed_seqs_cdhit_rep_seq_to_cluster.map ../R/cdhit_taxa_table_w_repseq.txt

#env file from Angela kent need to be mapped to the otu and taxa
##1. create the mapping file
#python $CODE/16s_fname_to_env_fname_to_sample_name.py all_16s_sample_names.txt > 16s_sample_name_to_env_table.map
##2. merging in R
## make taxa table, conver rep sequence to otu.
#Rscript ~/code/cdhit_clustering/renaming_taxa_rep_seq_to_otus.R cdhit_otu_taxa_filterbyconf.txt combined_renamed_seqs_cdhit_rep_seq_to_cluster.map ../R/taxa_table.txt
