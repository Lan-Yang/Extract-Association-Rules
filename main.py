import sys


def GetItemRow(file_name):
	item_list = set()
	row_list = list()
	item_freq = dict()
	# Read file once, record item set, row list and item frequency
	with open(file_name, 'r') as infile:
		for line in infile:
			tmp = line.split(',')
			row_list.append(list(set(tmp)))
			for item in tmp:
				if item in item_freq:
					item_freq.get(item) += 1
				else:
					item_freq[item] = 1
				item_list.add(item)
	return list(item_list), row_list, item_freq


def Apriori(file_name, min_sup, min_conf):
	item_list, row_list, item_freq = GetItemRow(file_name)
	total_num = len(row_list)

def main():
	if len(sys.argv) == 2:
		file_name = sys.argv[1]
		min_sup = float(raw_input('Minimum Support (between 0 and 1): '))
		min_conf = float(raw_input('Minimum Confidence (between 0 and 1): '))
	elif len(sys.argv) == 4:
		file_name = sys.arg[1]
		min_sup = float(sys.arg[2])
		min_conf = float(sys.arg[3])
	else:
		print 'Error Input Format'
		return

	# Check input
	if min_sup <= 1 and min_sup >= 0 and min_conf <= 1 and min_conf >= 0:
		pass
	else:
		print 'Error Input Format'
		return

	# Call a_priori algorithm
	Apriori(file_name, min_sup, min_conf)

if __name__ == '__main__':
	print len(sys.argv)
	main()