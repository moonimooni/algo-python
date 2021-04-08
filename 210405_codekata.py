def roman_to_num(s):
	answer = 0

	table = {
		'I' : 1,
		'V' : 5,
		'X' : 10,
		'L' : 50,
		'C' : 100,
		'D' : 500,
		'M' : 1000
	}

	i = 1

	while i < len(s):
		print
		if table[s[i]] > table[s[i-1]]:
			answer += (table[s[i]] - table[s[i-1]])
			i += 2
		else:
			answer += table[s[i-1]]
			i += 1
	if i == len(s):
		answer += table[s[i-1]]

	return answer

print(roman_to_num('MCMXCIV'))