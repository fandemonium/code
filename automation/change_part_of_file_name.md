for i in *_good.fa; do mv $i ${i//fastq_unique/fastq.fa_unique}; done
