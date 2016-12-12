for i in /mnt/data3/fan/rpf/April2016_ana/oid_html/fasta_files/metagenomes/*0
#for i in /mnt/data3/fan/rpf/April2016_ana/oid_html/fasta_files/test/*
	do cd $i
	for j in *.gbk
		do hmmsearch /mnt/data3/fan/rpf/April2016_ana/Hmm.ssu.hmm $j > $j.hmmsearch.txt
	done
done 
