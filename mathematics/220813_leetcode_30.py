import re
from functools import reduce
from itertools import permutations


# class Solution:
#     def findSubstring(self, s: str, words: list):
#         words_permutations = list(permutations(words, len(words)))

#         if len(words_permutations) == 0:
#             return []

#         combination_len = len(''.join(words_permutations[0]))

#         if len(words_permutations) == 1:
#             full_regex_pattern: str = ''.join(words_permutations[0])
#         else:
#             full_regex_pattern: str = reduce(lambda x, y:
#                                              ''.join(x) + '|' + ''.join(y), words_permutations)

#         full_regex = re.compile(full_regex_pattern)
#         return [i for i in range(len(s)) if full_regex.match(s[i:i+combination_len])]

def findSubstring(s: str, words: list):
    words_permutations = list(permutations(words, len(words)))
    print('1', words_permutations)
    if len(words_permutations) == 0:
        return []

    combination_len = len(''.join(words_permutations[0]))

    if len(words_permutations) == 1:
        full_regex_pattern: str = ''.join(words_permutations[0])
    else:
        full_regex_pattern: str = reduce(lambda x, y:
                                         ''.join(x) + '|' + ''.join(y), words_permutations)

    full_regex = re.compile(full_regex_pattern)

    return [i for i in range(len(s)) if full_regex.match(s[i:i+combination_len])]


findSubstring("bcabbcaabbccacacbabccacaababcbb", [
              "c", "b", "a", "c", "a", "a", "a", "b", "c"])
