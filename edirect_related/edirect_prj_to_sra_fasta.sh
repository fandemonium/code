prj_id=1
esearch -db sra -query $1 | efetch --format runinfo | cut -d ',' -f 1 | grep SRR | xargs fastq-dump --fasta
