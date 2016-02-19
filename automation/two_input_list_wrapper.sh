file="$1"
rho="$2"

while read line
do
	echo "processing: " $line
	while read number
	do
		RScript ~/Documents/repos/code/R/gnet_cc_subset.R $line $number /Users/fanyang/Box\ Sync/Manure\ Foaming/R_allsamples/foaming_status_cc/meta_w_genus_information.txt
	done < $rho
done < $file
