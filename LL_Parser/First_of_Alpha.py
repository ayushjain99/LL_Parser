def first_of_alpha(alpha,terminal,first_of_variables):
	ans = set()
	char = ''
	for i in range(len(alpha)):
		char_ = alpha[i]
		char = char + alpha[i]
		if(char_.isupper()):
			char = ''
			ans = ans.union(first_of_variables[char_])
			if ('^' in first_of_variables[char_]) and (i!=len(alpha)-1):
				ans = ans - {'^'}
			else:
				break
		else:
			if char in terminal:
				set_terminal = set([char])
				ans = ans.union(set_terminal)
				break
	return ans
