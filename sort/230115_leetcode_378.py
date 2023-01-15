# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/


from heapq import heappop, heappush
from itertools import chain
from typing import List


class Solution:
    # 내장 sort 쓰기
    # Runtime 172 ms Beats 94.75%
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     flattened = sorted(chain(*matrix))
    #     return flattened[k-1]

    # heap sort
    # Runtime 188 ms Beats 84.42%
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flattened = chain(*matrix)

        heap = []

        for val in flattened:
            heappush(heap, -val)

        while len(heap) > k:
            heappop(heap)

        return -heap[0]


s = Solution()
print(s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(s.kthSmallest([[-5]], 1))
