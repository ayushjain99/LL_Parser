def first_fn(production,terminal):
	ans = dict()
	for var in production:
		ans[var] = set()     # Initialize first of each var to an empty SET
	change = 1
	while change:
		change = 0
		for var in production:
			tmp_set = ans[var]
			for p in production[var]:
				length = len(p)
				char = ''
				for i in range(length):
					char_ = p[i]
					char = char + p[i]       # to find appr. terminal like in int
					# print(char)
					if (char_.isupper()):
						char = ''
						# char_ is a variable
						tmp_set = tmp_set.union(ans[char_])
						if ('^' in ans[char_]) and (i != length-1):	 # if variable is having null in its first
							tmp_set = tmp_set - {'^'}
						else:
							break
					else:
						if (char in terminal):
							set_terminal = set([char])                 #tmp set for terminal
							tmp_set = tmp_set.union(set_terminal)
							break

			if tmp_set != ans[var]:
				ans[var] = tmp_set
				change = 1
	return ans
