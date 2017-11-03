#esearch -db taxonomy -query "Cellulomonas persica [LNGE]" | elink -target nuccore | efetch -format docsum | xtract -pattern DocumentSummary -element Id Title Slen

##or 
#esearch -db taxonomy -query "Cellulomonas persica [Organism]" | elink -target nuccore | efetch -format docsum | xtract -pattern DocumentSummary -element Id Title Slen

org_list=$1
gene=$2

while read line
do
	echo "esearch -db taxonomy -query '"$line [LNGE]"' | elink -target nuccore | efetch -format docsum | xtract -pattern DocumentSummary -element Id Title Slen | grep '"$gene"' > ${line// /_}.gene.list"
done < $org_list


#efetch -db nuccore -id 944365106 -format fasta 
