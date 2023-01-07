# https://leetcode.com/problems/longest-palindrome/description/
# 짝수는 무조건 더한다.
# 홀수라면, 가능한 짝수만큼만 더한다.
# 홀수가 있다면, 1을 더 추가할 수 있다.

from collections import Counter
from functools import reduce


class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        s_counter_vals = s_counter.values()

        ret = 1 if any(val % 2 == 1 for val in s_counter_vals) else 0

        return ret + reduce(lambda acc, cur: acc + cur if cur % 2 == 0
                            else acc + cur - 1, s_counter_vals, 0)


s = Solution()

print(s.longestPalindrome('bananas'))
print(s.longestPalindrome('adam'))
print(s.longestPalindrome('aA'))
print(s.longestPalindrome('a'))
