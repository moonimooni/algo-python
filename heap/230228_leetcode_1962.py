# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from heapq import heappop, heappush
from math import floor
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for pile in piles:
            heappush(heap, -pile)
        for _ in range(k):
            popped = heappop(heap)
            heappush(heap, floor(popped / 2))

        return -sum(list(heap))


s = Solution()
print(s.minStoneSum([5, 4, 9], 2))
print(s.minStoneSum([4, 3, 6, 7], 3))
