infilename = "NYC_Causes_of_Death_original.csv"
outfilename = "NYC_Causes_of_Death.csv"

outfile = open(outfilename, "w")
with open(infilename, 'r') as infile:
	for line in infile:
		tmp = line.lower().split(',')
		if len(tmp) != 4:
			continue
		size = int(tmp[3])
		line = tmp[0] + ',' + tmp[1] + ',' + tmp[2] + '\n'
		for i in range(size):
			outfile.write(line)

outfile.close()
