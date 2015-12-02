import sys
import ijson


def get_l1(ss_ontology):
	for item in ijson.items(open(ss_ontology), ''):
		l1 = []
		for x in item["data"]:
			if "level1" in x and x["level1"] not in l1:
				l1.append(x["level1"])
		return l1			

def get_l2(ss_ontology):
	for item in ijson.items(open(ss_ontology), ''):
		l2 = []
		for x in item["data"]:
			if "level2" in x and x["level2"] not in l2:
				l2.append(x["level2"])
		return l2	

f = sys.argv[1]
t1 = get_l1(f)
t2 = get_l2(f)

for i in t1:
	print i
