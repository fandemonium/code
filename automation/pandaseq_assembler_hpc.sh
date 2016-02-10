#!/bin/bash
PANDASEQ="/mnt/research/rdp/public/RDP_misc_tools/pandaseq/pandaseq"
IN_DIR="/mnt/scratch/yangfan1/pitfoaming/Processed_mcrA/original"
OUT_DIR="/mnt/scratch/yangfan1/pitfoaming/Processed_mcrA/1_assembled"
OVERLAP="10" #16S:90
Q="25"
LEN="400" #16S:350

f="$1"

mkdir $OUT_DIR/sequences $OUT_DIR/assem_stats

while read tag
do 
    $PANDASEQ -N -o $OVERLAP -e $Q -l $LEN -F -d rbfkms -f $IN_DIR/"$tag"_*R1*.fastq -r $IN_DIR/"$tag"_*R2*.fastq 1> $OUT_DIR/sequences/"$tag"_assembled.fastq 2> $OUT_DIR/assem_stats/"$tag"_assembled_stats.txt 
done < $f
