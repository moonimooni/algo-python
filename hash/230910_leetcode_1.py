# https://leetcode.com/problems/two-sum/

from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map: Dict[int, List[int]] = dict()
        for i, num in enumerate(nums):
            if num in hash_map:
                return [hash_map[num], i]
            else:
                hash_map[target-num] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
