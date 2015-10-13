#!/bin/bash

f="$1"

for i in pool_*
do 
	while read tag
	do 
		~/RDP_Assembler/pandaseq/pandaseq -N -o 80 -e 25 -l 350 -F -d rbfkms -f /mnt/data3/fan/pitfoaming/$i/fastqs/*_"$tag"_*R1*.fastq -r /mnt/data3/fan/pitfoaming/$i/fastqs/*_"$tag"_*R2*.fastq 1> /mnt/data3/fan/pitfoaming/$i/assembled/"$tag"_assembled.fastq 2> /mnt/data3/fan/pitfoaming/$i/assembled/"$tag"_assembled_stats.txt
	done < $f
done
