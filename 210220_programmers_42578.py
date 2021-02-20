# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter
from functools import reduce
from operator import mul
from collections import defaultdict

# clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]

# def solution(clothes):
#     closet = Counter([ctg for name, ctg in clothes])
#     values = [x+1 for x in closet.values()]
#     return reduce(lambda x, y: x * y, values) - 1

# def solution(clothes):
#     closet = defaultdict(int)
#     for name, ctg in clothes:
#         closet[ctg] += 1
#     values = [x+1 for x in closet.values()]
#     return reduce(lambda x,y: x*y, values) - 1

def solution(clothes):
    closet = defaultdict(int)
    for name, ctg in clothes:
        closet[ctg] += 1
    values = [x+1 for x in closet.values()]
    return reduce(mul, values) - 1
