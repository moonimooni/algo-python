# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        default_res = -1
        sorted_nums = sorted(nums)
        max_possible_res = len(nums)

        while max_possible_res > 0:
            if max_possible_res == self.__binary_search(sorted_nums, max_possible_res, 0, len(sorted_nums) - 1):
                return max_possible_res

            max_possible_res -= 1

        return default_res

    # 소팅된 nums 배열 안에서 searching_value 값 중 가장 작은 index를 구해야 함
    def __binary_search(self, nums: List[int], searching_value: int, left_idx: int, right_idx: int):
        if left_idx > right_idx:
            return None
        binary_idx = left_idx + (right_idx - left_idx) // 2

        if searching_value <= nums[binary_idx]:
            if searching_value > nums[binary_idx - 1] or not binary_idx:
                return len(nums[binary_idx:])
            else:
                return self.__binary_search(nums, searching_value, left_idx, binary_idx + 1)

        elif searching_value > nums[binary_idx]:
            return self.__binary_search(nums, searching_value, binary_idx + 1, right_idx)


s = Solution()
print(s.specialArray([3, 5]))
print(s.specialArray([0, 0]))
print(s.specialArray([0, 4, 3, 0, 4]))
