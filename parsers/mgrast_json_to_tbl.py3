import json
import sys
import re

f = json.load(open(sys.argv[1]))
data = f["data"]
#print(data[0].keys())

for i in range(0, len(data)):
	env = data[i]["env_package"]
	data_type = data[i]["investigation_type"]
	org = data[i]["organization"]
	mgm = data[i]["metagenome_id"]
	loc = data[i]["location"]
	feature = data[i]["feature"]
	prj = data[i]["project_name"]
	country = data[i]["country"]
	material = data[i]["material"]
	sample_name = data[i]["sample_name"]
	if "target_gene" in data[i]:
		target_gene = data[i]["target_gene"]
	else:
		target_gene = "NA"
	if "ncbi_id" in data[i]:
		ncbi_id = data[i]["ncbi_id"]
	else:
		ncbi_id = "NA"
	print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(org, data_type, prj, env, feature, material, loc, country, sample_name, mgm, target_gene, ncbi_id))
