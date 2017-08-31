for i in *.gz; do paste -d : <(echo $i) <(zcat $i | grep -c "@MISEQ:"); done > ../summaries/raw_read_counts.txt
