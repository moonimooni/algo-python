from itertools import combinations

def solution(numbers):
    pairs = combinations(numbers, 2)
    return sorted(list(set([sum(pair) for pair in pairs])))