# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      # 근시안적 풀이..ㅋㅋ
        rectangle = 0
        # cur_height = None
        # before = -1
        # for height in heights:
        #     if cur_height is None:
        #         cur_height = height
        #     cur_height = height if height < before else before
        #     rectangle = rectangle + cur_height if height < rectangle else height
        #     before = height
        # return rectangle


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea([2, 4]))
