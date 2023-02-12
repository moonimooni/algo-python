# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        ret, vps_depth = 0, 0
        for char in s:
            if char == '(':
                vps_depth += 1
            elif char == ')':
                vps_depth -= 1
            ret = max(ret, vps_depth)
        return ret


s = Solution()
print(s.maxDepth('(1+(2*3)+((8)/4))+1'))
# (()(()))
print(s.maxDepth('(1)+((2))+(((3)))'))
print(s.maxDepth('8*((1*(5+6))*(8/6))'))
