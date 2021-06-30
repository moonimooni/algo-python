from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        coms = permutations(nums,len(nums))
        return [list(com) for com in coms]