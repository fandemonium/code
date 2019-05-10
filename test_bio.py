import sys

for lines in open(sys.argv[1], 'rU'):
	key, value = lines[:2], lines[5:].rstrip()
	if key == 'RN':
		print(value)
		rns = lines.split("\n")[0]
	        words = rns.rsplit(" ", 2)
	        number = words[0]
        	assert number.startswith('[') and number.endswith(']'), "Missing brackets %s" % number
        	reference.number = int(number[1:-1])
        	if len(words) == 2:
                	evidence = words[1]
                	assert evidence.startswith('{') and evidence.endswith('}'), "Missing braces %s" % evidence
                	reference.evidence = evidence[1:-1].split('|')
        	elif len(words) > 2:
                	evidence = " ".join(words[1:])
                	assert evidence.startswith('{') and evidence.endswith('}'), "with multiple reference: %s. Missing braces %s" % evidence
                	reference.evidence = evidence[1:-1].split('|')
			print(reference.number, reference.evidence)
