## automation script for combine_desc_clstr.py

for i in *; 
do 
	python ~/Documents/Fan/code/combine_desc_clstr.py /Users/metagenomics/Documents/Fan/spruce_meta_protease/blast_xander_q25/prot_merged_cdhit/counts/x704.$i.prot_cdhit.fasta.clstr.count /Users/metagenomics/Documents/Fan/spruce_meta_protease/blast_xander_q25/parsed/x704.$i.prot_cdhit.fasta.blast.desc.e-3 > /Users/metagenomics/Documents/Fan/spruce_meta_protease/blast_xander_q25/bdesc_counts/x704.$i.desc_counts.combined
done
