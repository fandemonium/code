#esearch -db taxonomy -query "Cellulomonas persica [LNGE]" | elink -target nuccore | efetch -format docsum | xtract -pattern DocumentSummary -element Id Title Slen

##or 
#esearch -db taxonomy -query "Cellulomonas persica [Organism]" | elink -target nuccore | efetch -format docsum | xtract -pattern DocumentSummary -element Id Title Slen

org_list=$1
gene=$2

while read line
do
	echo "esearch -db taxonomy -query '"$line [LNGE]"' | elink -target nuccore | efetch -format docsum | xtract -pattern DocumentSummary -element Gi Title Slen | grep '"$gene"' > ${line// /_}.gene.list"
done < $org_list > get_gene_id.sh

#`$gene`: ITS: "internal transcribed spacer"
#`$gene`: 16S: "16S"

bash get_gene_id.sh #don't over load the API request...
find . -type f -size 0 -delete #delete empty files. 
cat *.list | cut -f 1 | sort | uniq > ../ncbi.id
cd ../
mkdir ncbi_fas
while read line; do echo "efetch -db nuccore -id '"$line"' -format fasta > ncbi_fas/$line.fa"; done < ../ncbi.id > get_ncbi_gene_fa.sh
bash get_ncbi_gene_fa.sh


#efetch -db nuccore -id 944365106 -format fasta 

