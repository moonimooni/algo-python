def get_len_of_str(s):
	hash_map = dict()
	longest_len, now_len = 0, 0

	for char in s:
		if char in hash_map:
			now_len = len(hash_map)
			if longest_len < now_len:
				longest_len = now_len
				hash_map = dict()
				hash_map[char] = True
		else:
			hash_map[char] = True
	
	if longest_len < len(hash_map):
		return len(hash_map)
	return longest_len

# def get_len_of_str(s):
# 	words = list()
# 	longest_len = 0
# 	for i in range(len(s)):
# 		if s[i] not in words:
# 			words.append(s[i])
# 		else:
# 			if len(words) > longest_len:
# 				longest_len = len(words)
# 				words = [s[i]]
	
# 	if longest_len < len(words):
# 		return len(words)
# 	return longest_len


print(get_len_of_str('sttrg'))