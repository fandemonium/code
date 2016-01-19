#!/bin/bash
PANDASEQ="/mnt/research/rdp/public/RDP_misc_tools/pandaseq/pandaseq"
IN_DIR="/mnt/scratch/yangfan1/pitfoaming/Processed_16s/original"
OUT_DIR="/mnt/scratch/yangfan1/pitfoaming/Processed_16s/1_assembled"

f="$1"

mkdir $OUT_DIR/sequences $OUT_DIR/assem_stats

while read tag
do 
    $PANDASEQ -N -o 80 -e 25 -l 350 -F -d rbfkms -f $IN_DIR/"$tag"_*R1*.fastq -r $IN_DIR/"$tag"_*R2*.fastq 1> $OUT_DIR/sequences/"$tag"_assembled.fastq 2> $OUT_DIR/assem_stats/"$tag"_assembled_stats.txt 
done < $f
