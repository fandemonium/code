## automation script for combine_desc_clstr.py

for i in *; 
do 
	python ~/Documents/Fan/scratch/code/combine_desc_clstr.py /Users/metagenomics/Documents/Fan/scratch/parsed_files/clstr_parsed/x75_"$i".clstr.parsed /Users/metagenomics/Documents/Fan/scratch/parsed_files/blast_parsed/x75_"$i"_nucl_cdhit.blast.desc.parsed > /Users/metagenomics/Documents/Fan/scratch/parsed_files/combined/x75_"$i".combined
done
