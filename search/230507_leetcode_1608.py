# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        not_special_array_flag = -1

        sorted_nums = sorted(nums)
        left_idx, right_idx = 0, len(sorted_nums)

        while left_idx <= right_idx:
            mid_idx = left_idx + (right_idx - left_idx) // 2

            if mid_idx >= len(sorted_nums):
                break

            possible_special_num = len(sorted_nums) - mid_idx

            if possible_special_num <= sorted_nums[mid_idx]:
                if possible_special_num > sorted_nums[mid_idx - 1] or not mid_idx:
                    return possible_special_num
                else:
                    right_idx = mid_idx - 1

            else:
                left_idx = mid_idx + 1

        return not_special_array_flag


s = Solution()
print(s.specialArray([3, 5]))
print(s.specialArray([0, 0]))
print(s.specialArray([0, 4, 3, 0, 4]))
