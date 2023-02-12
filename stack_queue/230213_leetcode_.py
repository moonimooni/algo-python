# https://leetcode.com/problems/decode-string/

from functools import reduce


class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                command = ''
                popped = stack.pop()
                while popped != '[':
                    command = popped + command
                    popped = stack.pop()
                repeat = int(stack.pop())
                stack.append(repeat * command)
        return reduce(lambda acc, cur: acc + cur, stack)


s = Solution()
print(s.decodeString('3[a]2[bc]'))
print(s.decodeString('3[a2[c]]'))
