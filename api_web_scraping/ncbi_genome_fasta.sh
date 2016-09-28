while read gi
do
	curl "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id="$gi"&rettype=fasta&retmode=text" > $2/$gi.fa
done < $1
