from First_of_Alpha import first_of_alpha
# Will work for now
def follow_fn(production,terminal,start_symbol,first_of_variables):
	ans = dict()
	for var in production:
		ans[var] = set()
	#ans[start_symbol] = {'$'}
	change = 1
	while change:
		change = 0
		for var in production:
			tmp_set = ans[var]
			if(var == start_symbol):
				tmp_set = tmp_set.union({'$'})
			for lhs in production:
				for p in production[lhs]:
					if p.find(var)<0:
						continue
					elif p.find(var)<len(p)-1:
						alpha = p[p.find(var)+1]
						#print(var + " " + alpha)
						if '^' not in first_of_alpha(alpha,terminal,first_of_variables):
							tmp_set = tmp_set.union(first_of_alpha(alpha,terminal,first_of_variables))
						else:
							tmp_set = tmp_set.union(first_of_alpha(alpha,terminal,first_of_variables))
							tmp_set = tmp_set - {'^'}
							tmp_set = tmp_set.union(ans[lhs])
					else:
						tmp_set = tmp_set.union(ans[lhs])
			if tmp_set != ans[var]:
				ans[var] = tmp_set
				change = 1
	return ans
