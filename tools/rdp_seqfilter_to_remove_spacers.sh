## for forward primer in R1

## create a folder to keep all outputs together
mkdir R1_spacer_removal

## make sure you are in the directory where all of the sample R1 reads are:
## you will also need to make sure you can call function SeqFilters.jar directly or specify the pathway to it. 
## right now, the code is tailored to return everything, including bad quality scores. But you can reset it by changing "--min-length" and "Q" score
## The outputs will be individual directories named after your R1 samples

for i in sample*_R1.txt
do
	java -jar tools/RDPTools/SeqFilters.jar --forward-primers GAAKRGTTYGATYNTGGCTCAG --max-forward 2 --seq-file $i --min-length 1 -Q 0 --keep-primer true --outdir R1_spacer_removal/"$i"_rm_spacer
done

## navigate into "R1_spacer_removal"
cd R1_spacer_removal

## you only need the sequences with spacer removed.
## mv sequences with spaver removed out to "R1_spacer_removal" and rename it to match with your R1 samples
## then remove the folders with unused data
for j in sample*_R1*_rm_spacer
do
	mv $j/result_dir/NoTag/NoTag_trimmed.fastq ./$j.fastq
	rm -r $j
done

## finally, remove empty files if there is any
find . -size 0 -delete
