def get_prefix(strs):
	answer = ''

	if not strs:
		return answer

	shortest_word = min(strs)

	for i in range(len(shortest_word)):
		for j in range(len(strs)):
			if j == (len(strs) - 1):
				answer += shortest_word[i]
			elif shortest_word[i] == strs[j][i]:
				continue
			else:
				return answer
	return answer

print(get_prefix(['flower', 'flue', 'fly']))