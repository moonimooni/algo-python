# from collections import Counter

# def solution(nums):
#     answer = 0
#     select_maximum = len(nums) // 2
#     sets = Counter(nums)
#     if select_maximum < len(sets.keys()):
#         return select_maximum
#     return len(sets.keys())

def solution(nums):
    pocketmons = len(list(set(nums)))
    choice_max = len(nums) // 2
    if choice_max < pocketmons:
        return choice_max
    return pocketmons

# 다른 사람 풀이
def solution(nums):
    pocketmons = len(list(set(nums)))
    choice_max = len(nums) // 2
    return min(choice_max, pocketmons)
