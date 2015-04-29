infile = open('in.csv', 'r')
sample = infile.readlines()
infile.close()

outfile = open('Parking_Violations_Issued_2013_2014.csv', 'w')

count = 0

for line in sample:
	if count == 5000:
		break
	line.rstrip()
	tokens = line.split(',')
	if int(tokens[8]) != 0 and tokens[3] != '' and tokens[6] != '' and tokens[4] != '' and tokens[7] != '' and tokens[0] != '99' and tokens[1] != '999':
		count += 1
		outfile.write(','.join(tokens[1:]))

outfile.close()