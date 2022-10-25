# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter


class Solution:

    """
    # EXAMPLE
    # s = 'AD0BEC0DEBANC'
    # t = 'ABC'
    # should return 'BANC'
    """

    def minWindow(self, s: str, t: str) -> str:
        required_counter, window_counter = Counter(t), Counter()
        pointer_left = pointer_right = 0
        window_left = window_right = None

        required_length = len(t)

        while pointer_left < len(s):

            while required_length != 0 and pointer_right < len(s):
                right_char = s[pointer_right]
                window_counter[right_char] += 1

                if required_counter[right_char] >= window_counter[right_char]:
                    required_length -= 1

                pointer_right += 1

            left_char = s[pointer_left]

            if required_length == 0:
                if window_left is None or window_right - window_left > pointer_right - pointer_left:
                    window_left, window_right = pointer_left, pointer_right

            window_counter[left_char] -= 1

            if required_counter[left_char] > window_counter[left_char]:
                required_length += 1

            pointer_left += 1

        return s[window_left:window_right] if window_left is not None else ''


sol = Solution()
print(sol.minWindow('AD0BEC0DEBANC', 'ABC'))
print(sol.minWindow('a', 'a'))
print(sol.minWindow('a', 'aa'))
print(sol.minWindow('ab', 'a'))
print(sol.minWindow('aa', 'aa'))
print(sol.minWindow('acbbaca', 'aba'))
print(sol.minWindow('bdab', 'ab'))
print(sol.minWindow('cabwefgewcwaefgcf', 'cae'))
