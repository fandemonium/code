1. build bowtie index:
```
# conver gbk to fa file
python ../repos/code/genbank-fan/gbk_to_fa.py pax.gbk pax.fa
# pax.fa's header need to be modified to make sure that it matches reference index
# in this case, remove everything after space, leaving only ">NC_014228.1"
# build index using the fa
bowtie2-build -f pax.fa pax_operon
```

2. run bowtie2 (don't do quality check if using pair-ended sequences
```
cd S18803-036/
bowtie2 -x ../bowtie2_db/pax_operon --very-sensitive-local -1 HiSeq_1787_3_T7029-T5020_1.fastq.gz -2 HiSeq_1787_3_T7029-T5020_2.fastq.gz -S S18803-036_pax.sam
```

3. converting sam file to bam
```
samtools view -S -F4 -b S18803-036_pax.sam > S18803-036_pax.bam 
# check samfile SQ header, make sure it's the same as the pax.fa
samtools view -H S18803-036_pax.bam
# sorted bam
samtools sort S18803-036_pax.bam -o S18803-036_pax.sorted.bam
```

4. mpileup
```
samtools mpileup -Q 20 -f ../pax.fa S18803-036_pax.sorted.bam > S18803-036_pax.mapping_coverage.txt
# summary
python ../../repos/glowing_sakana/misc/mpileup_ref_coverage.py S18803-036_pax.mapping_coverage.txt ../pax.fa > S18803-036_pax.mapping_coverage.summary
```
