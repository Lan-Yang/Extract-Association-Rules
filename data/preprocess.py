import re

infilename = "NYC_Causes_of_Death_original.csv"
outfilename = "NYC_Causes_of_Death.csv"

outfile = open(outfilename, "w")
with open(infilename, 'r') as infile:
	for line in infile:
		tmp = re.split(r'[\s,\(\)\'\"]+', line.lower())
		tmp = filter(lambda t: t != '', tmp)
		line = ','.join(tmp)
		outfile.write(line+'\n')

outfile.close()
