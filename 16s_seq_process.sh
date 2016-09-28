## in `00_original_w_rerun` directory:
ls *.gz > ../sample_list.txt

cd ..
rev sample_list.txt | cut -d . -f 4- | rev | sort | uniq > sample_list_names.txt

mkdir 1_rdp_pandaseq
cd 1_rdp_pandaseq
mkdir assembled stats
while read i; do /mnt/research/rdp/public/RDP_misc_tools/pandaseq/pandaseq -N -o 10 -e 25 -F -d rbfkms -l 250 -L 280 -f ../00_original_w_rerun/$i.R1.fastq.gz -r ../00_original_w_rerun/$i.R2.fastq.gz 1> assembled/"$i"_250-280.fastq 2> stats/"$i"_assembled_stats.txt; done < ../sample_list_names.txt

mkdir 2_quality_check
cd 2_quality_check/
mkdir fastq_q25 fasta_q25 chimera_removal
cd ../1_rdp_pandaseq
for i in *.fastq; do java -jar /mnt/research/rdp/public/RDPTools/SeqFilters.jar -Q 25 -s $i -o ../../2_quality_check/fastq_q25/ -O $i.q25; done

cd fastq_q25
for i in *.q25; do mv $i/NoTag/NoTag_trimmed.fastq $i/NoTag/$i.fastq; done
mv */NoTag/*.fastq .
for i in *.fastq; do python ~/repos/code/fastq_to_fasta.py $i ../fasta_q25/$i.fa; done

cd ../fasta_q25
cat *.fa >> ../chimera_removal/all_combined_q25.fa

cd chimera_removal
/mnt/research/rdp/public/thirdParty/usearch8.1.1831_i86linux64 -derep_fulllength all_combined_q25.fa -fastaout all_combined_q25_unique.fasta -sizeout
/mnt/research/rdp/public/thirdParty/usearch8.1.1831_i86linux64 -sortbysize all_combined_q25_unique.fasta -fastaout all_combined_q25_sorted.fa -minsize 2
/mnt/research/rdp/public/thirdParty/usearch8.1.1831_i86linux64  -cluster_otus all_combined_q25_sorted.fa -id 0.985 -otus all_combined_q25_chim_denovo.fa
#chimera removal using rdp training set
/mnt/research/rdp/public/thirdParty/usearch8.1.1831_i86linux64 -uchime_ref all_combined_q25_chim_denovo.fa -db ~/databases/RDPClassifier_16S_trainsetNo16_rawtrainingdata/trainset16_022016.fa -strand plus -chimeras all_combined_q25_chim_denovo_ref.chimeras -nonchimeras all_combined_q25_chim_denovo_ref_good.fa
# or chimera removal using rdp full set
/mnt/research/rdp/public/thirdParty/usearch8.1.1831_i86linux64 -uchime_ref all_combined_q25_chim_denovo.fa -db ~/databases/current_Bacteria_unaligned.fa -strand plus -chimeras all_combined_q25_chim_denovo_ref_fullrdp.chimeras -nonchimeras all_combined_q25_chim_denovo_ref_good_fullrdp.fa

cd ../fastq_q25
for i in *.fastq; do /mnt/research/rdp/public/thirdParty/usearch8.1.1831_i86linux64 -usearch_global $i -db ../chimera_removal/all_combined_q25_chim_denovo_ref_good_fullrdp.fa -strand plus -id 0.985 -matched ../final_good_seqs/"$i"_finalized.fa;done

bash ~/repos/code/cdhit_clustering/cdhit_clustering_pipeline_hpc.sh 
