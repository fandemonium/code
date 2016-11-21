#DIR="/mnt/data3/fan/rpf/April2016_ana/oid_html/genbank_files/test"
DIR="/mnt/data3/fan/rpf/April2016_ana/oid_html/fasta_files/metagenomes"

for i in $DIR/*
	do cd $i
           for j in *.txt
	        do while read line
			do echo "/mnt/data3/fan/edirect/efetch -db nuccore -id $line -format fasta > $i/$line.gbk" 
		done < $j
	done 
done > /mnt/data3/fan/rpf/April2016_ana/oid_html/fasta_files/edirect_contig_acc_get_fa_commands.sh
