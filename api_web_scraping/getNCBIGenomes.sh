#!/bin/bash

TAX=(bacteria archaea plasmid protozoa viral)
SRC=(genbank refseq)

for TAXON in ${TAX[@]}; do
  for REF in ${SRC[@]}; do
    mkdir -p /ngsassembly/hlin/cas9/dev/bpb/ncbi_genomes/$TAXON/$REF
    cd /ngsassembly/hlin/cas9/dev/bpb/ncbi_genomes/$TAXON/$REF
    rm assembly_summary.txt
    # get the master list of ncbi info
    wget ftp://ftp.ncbi.nlm.nih.gov/genomes/$REF/$TAXON/assembly_summary.txt
    # see how different the numbers are
    wc -l assembly_summary.txt
    grep -c -P '\tlatest\t' assembly_summary.txt
    # 1) pull out ftp dir for 'latest' versions of genomes with awk
    # 2) append the name of the file to retrieve using sed based upon the directory name
    awk -F "\t" '$11=="latest"{print $20}' assembly_summary.txt | sed -r 's#(ftp://ftp.ncbi.nlm.nih.gov/genomes/all/)(GC[AF]_.+)#\1\2/\2_genomic.gbff.gz#' > ftpdirpath
    wget -i ftpdirpath --no-clobber --quiet --no-host-directories --no-parent --no-directories
  done
done

