##automation
while read id; do ~/usearch -cluster_agg rpf_w_refs.fa -treeout uclust_avg_linkage/rpf_w_refs_"$id".nwk -clusterout rpf_w_refs_"$id"_cluster.txt -id $id -linkage avg; done < uclust_id2.txt

##uclust_id2.txt looks like this
0.50
0.55
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.97
0.99

##usearch alone
usearch -cluster_agg seqs.fasta -treeout tree.phy -clusterout clusters.txt -id 0.65 -linkage avg
