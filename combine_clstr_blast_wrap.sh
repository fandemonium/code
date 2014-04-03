for i in *; 
do 
	python ~/Documents/Fan/code/combine_desc_clstr.py /Users/metagenomics/Documents/Fan/scratch/parsed_files/clstr_parsed/x701_"$i".clstr.parsed /Users/metagenomics/Documents/Fan/scratch/parsed_files/blast_parsed_no_restriction/x701_"$i"_nucl_cdhit.blast.desc.parsed > /Users/metagenomics/Documents/Fan/scratch/parsed_files/combined_no_restriction/x701_"$i".combined
done
