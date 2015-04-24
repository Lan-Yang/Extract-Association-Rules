import sys

def JoinSet(current_set, k):
	_current_set = set()
	for i in current_set:
		for j in current_set:
			tmp_set1 = set()
			for item in i:
				tmp_set1.add(item)
			tmp_set2 = set()
			for item in j:
				tmp_set2.add(item)
			tmp = tmp_set1.union(tmp_set2)
			if len(tmp) == k:
				_current_set.add(tuple(tmp))

	return _current_set

def MinSuppSet(current_set, row_list, min_sup, freq_set):
	_current_set = set()
	total_num = len(row_list)
	tmp_dict = dict()

	# Calculate frequence for each item in current set
	for i in range(total_num):
		for j in current_set:
			# print j
			if set(j).issubset(row_list[i]):
				if j in tmp_dict:
					tmp_dict[j] += 1
				else:
					tmp_dict[j] = 1

	for k,v in tmp_dict.iteritems():
		support = v*1.0/total_num
		if support >= min_sup:
			_current_set.add(k)
			freq_set[k] = support

	return _current_set, freq_set


def GetItemRow(file_name):
	item_set = set()
	row_list = list()
	item_freq = dict()
	# Read file once, record 1-item set, row list and 1-item frequency
	with open(file_name, 'r') as infile:
		for line in infile:
			line = line.rstrip()
			tmp = line.split(',')
			row_list.append(set(tmp))
			for item in tmp:
				if item in item_freq:
					item_freq[item] += 1
				else:
					item_freq[item] = 1
				item_set.add(item)
	return list(item_set), row_list, item_freq


def Apriori(file_name, min_sup, min_conf):
	item_set, row_list, item_freq = GetItemRow(file_name)
	freq_set = dict()
	rules = dict()
	# Get first C set
	c_one = set()
	total_num = len(row_list)

	# print item_freq

	for k,v in item_freq.iteritems():
		support = v*1.0/total_num
		if support >= min_sup:
			k = (k,)
			c_one.add(k)
			freq_set[k] = support
	# Get c_k set
	# current_set is a set, and each element in it is a tuple
	k = 2
	current_set = c_one

	while len(current_set) > 0:
		current_set = JoinSet(current_set, k)
		current_set, freq_set = MinSuppSet(current_set, row_list, min_sup, freq_set)
		k += 1

	# Generate rules
	for item_set,v in freq_set.iteritems():
		if len(item_set) > 1:
			item_set = set(item_set)
			for rhs in item_set:
				copy = set(item_set)
				copy.remove(rhs)
				lhs = tuple(copy)
				# Calculate confidence of rule
				conf = v*1.0/freq_set[lhs]
				if conf >= min_conf:
					try:
						rules[lhs][rhs] = conf
					except Exception:
						rules[lhs] = {rhs: conf}

	return freq_set, rules

def Print(freq_set, rules, min_sup, min_conf):
	outfile = open("output.txt", 'w')
	# Write frequent itemsets
	# print '==Frequent itemsets (min_sup= {}%)\n'.format(min_sup)
	outfile.write('==Frequent itemsets (min_sup={}%)\n'.format(int(min_sup * 100)))
	for item_set,v in freq_set.iteritems():
		item_set = list(item_set)
		outfile.write('[')
		for i in item_set[:-1]:
			outfile.write('%s,' % i)
		outfile.write('%s' % item_set[-1])
		outfile.write('], {}%\n'.format(int(v * 100)))
	# Write high-confidence association rules
	outfile.write('\n==High-confidence association rules (min_conf={}%)\n'.format(int(min_conf * 100)))
	for k1,v1 in rules.iteritems():
		k1 = list(k1)
		for k2,v2 in v1.iteritems():
			rhs = k2
			conf = v2[0]
			supp = v2[1]
			outfile.write('[')
			for i in k1[:-1]:
				outfile.write('%s,' % i)
			outfile.write('%s' % i)
			outfile.write('] => [%s] (Conf: {}%, Supp: {}%)\n'.format(rhs, int(conf * 100), int(supp * 100)))
	outfile.close()

def main():
	if len(sys.argv) == 2:
		file_name = sys.argv[1]
		min_sup = float(raw_input('Minimum Support (between 0 and 1): '))
		min_conf = float(raw_input('Minimum Confidence (between 0 and 1): '))
	elif len(sys.argv) == 4:
		file_name = sys.argv[1]
		min_sup = float(sys.argv[2])
		min_conf = float(sys.argv[3])
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
	freq_set, rules = Apriori(file_name, min_sup, min_conf)

	print rules

	print freq_set

	# Print result
	Print(freq_set, rules, min_sup, min_conf)

if __name__ == '__main__':
	print len(sys.argv)
	main()