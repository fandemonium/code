for i in pool_*
	do
	cd /mnt/data3/fan/pitfoaming/$i/assembled
	for j in *.fastq
		do usearch -fastq_filter $j -fastq_maxee 0.5 -fastaout /mnt/data3/fan/pitfoaming/$i/quality_filtered/"$i"_"$j"_maxee_0.5.fasta 
	done
	cd /mnt/data3/fan/pitfoaming/
done
