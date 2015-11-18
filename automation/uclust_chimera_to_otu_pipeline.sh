#mkdir all_pool_quality_trimmed
#mv pool_1*/quality_filtered/*.fasta all_pool_quality_trimmed/

#cd /mnt/data3/fan/pitfoaming
#mkdir chimera_removal chimera_removal/derep chimera_removal/sorted chimera_removal/de_novo chimera_removal/ref chimera_removal/ref/stats chimera_removal/ref/chimeras chimera_removal/ref/good_otus good_seqs

#cd /mnt/data3/fan/pitfoaming/all_pool_quality_trimmed
#for i in *.fasta; do usearch -derep_fulllength $i -fastaout /mnt/data3/fan/pitfoaming/chimera_removal/derep/"$i"_unique.fasta -sizeout; done

#cd /mnt/data3/fan/pitfoaming/chimera_removal/derep
#for i in *_unique.fasta; do usearch -sortbysize $i -fastaout /mnt/data3/fan/pitfoaming/chimera_removal/sorted/"$i"_sorted.fa -minsize 2; done

#cd /mnt/data3/fan/pitfoaming/chimera_removal/sorted
#for i in *.fa; do usearch -cluster_otus $i -otu_radius_pct 3.0 -otus /mnt/data3/fan/pitfoaming/chimera_removal/de_novo/"$i"_otu1.fa; done

#cd /mnt/data3/fan/pitfoaming/chimera_removal/de_novo
#for i in *_otu1.fa; do usearch -uchime_ref $i -db /mnt/data3/qiime-db/gold.fa -uchimeout /mnt/data3/fan/pitfoaming/chimera_removal/ref/stats/"$i".uchime -strand plus -selfid -mindiv 1.5 -mindiffs 5 -chimeras /mnt/data3/fan/pitfoaming/chimera_removal/ref/chimeras/"$i"_chimera.fa -nonchimeras /mnt/data3/fan/pitfoaming/chimera_removal/ref/good_otus/"$i"_otu2.fa; done
## new one:
for i in *.fa; do usearch -uchime_ref $i -db /mnt/data3/fan/RDPinfernal1.1Traindata/RDPClassifier_16S_trainsetNo15_rawtrainingdata/trainset15_092015.fa -strand plus -chimeras /mnt/data3/fan/pitfoaming/2_rdp_uchime/chime_ref/chimeras/"$i"_chimera.fa -nonchimeras /mnt/data3/fan/pitfoaming/2_rdp_uchime/chime_ref/ref_good/"$i"_ref_good.fa; done

###################################################################################
## if you want to use modeled alignment to pick otu (e.g., rdp tools), do this:  ##
###################################################################################
#cd /mnt/data3/fan/pitfoaming/all_pool_quality_trimmed
#for i in *.5.fasta; do usearch  -usearch_global $i -db /mnt/data3/fan/pitfoaming/chimera_removal/ref/good_otus/"$i"_unique.fasta_sorted.fa_otu1.fa_otu2.fa -strand plus -id 0.985 -matched /mnt/data3/fan/pitfoaming/good_seqs/"$i"_finalized.fa; done

###################################################################################
## if use uclust/uparse commands, generate master otus directly, do this:        ##
###################################################################################
#mkdir /mnt/data3/fan/pitfoaming/chimera_removal/master_otus
#cd /mnt/data3/fan/pitfoaming/chimera_removal/master_otus
#cat /mnt/data3/fan/pitfoaming/chimera_removal/ref/good_otus/*.fa > combined_good_otus.fa
#usearch -derep_fulllength combined_good_otus.fa -fastaout combined_good_otus.fa_derep.fa -sizeout
#usearch -sortbysize combined_good_otus.fa_derep.fa -fastaout combined_good_otus.fa_derep.fa_sorted.fa -minsize 1
#usearch -cluster_otus combined_good_otus.fa_derep.fa_sorted.fa -otu_radius_pct 3.0 -uparse_break -100.0 -otus final_otus.fa -relabel OTU_

#mkdir /mnt/data3/fan/pitfoaming/final_mapping /mnt/data3/fan/pitfoaming/final_mapping/mapping
#cd /mnt/data3/fan/pitfoaming/all_pool_quality_trimmed
#for i in *.5.fasta; do usearch -usearch_global $i -db /mnt/data3/fan/pitfoaming/chimera_removal/master_otus/final_otus.fa -strand plus -id 0.97 -uc /mnt/data3/fan/pitfoaming/final_mapping/mapping/$i.mapped.uc; done

#usearch -utax /mnt/data3/fan/pitfoaming/chimera_removal/master_otus/final_otus.fa -db /mnt/data3/qiime-db/rdp_16s.fa -taxconfs /mnt/data3/qiime-db/rdp_16s.tc -strand both -utaxout /mnt/data3/fan/pitfoaming/final_mapping/otu_taxa.txt

#cd /mnt/data3/fan/pitfoaming/final_mapping/mapping/
#mkdir /mnt/data3/fan/pitfoaming/final_mapping/add_sample_names
#for i in *.uc; do python /mnt/data3/fan/code/usearch_map_uc_parser.py $i > ../add_sample_names/"$i".sample; done
#cat /mnt/data3/fan/pitfoaming/final_mapping/add_sample_names/*.sample > /mnt/data3/fan/pitfoaming/final_mapping/combined_samples_with_file_names.txt

python /mnt/data3/fan/code/uclust_py/uc2otutab.py /mnt/data3/fan/pitfoaming/final_mapping/combined_samples_with_file_names.txt > /mnt/data3/fan/pitfoaming/final_mapping/otu_table.txt

