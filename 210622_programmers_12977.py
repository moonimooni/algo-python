# 옛날 풀이
def isPrime(num):
    if num == 2:
        return True
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

def solution(nums):
    sums = []

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sums.append(nums[i]+nums[j]+nums[k])
    return len(list(filter(isPrime, sums)))
            

# 최근 풀이
from itertools import combinations
from math import sqrt, trunc

def isPrime(num):
    max_divisor = trunc(sqrt(num))+1
    for i in range(2, max_divisor):
        if not num % i:
            return False
    return True

def solution(nums):
    answer = 0
    sets = combinations(nums, 3)
    for i in sets:
        if isPrime(sum(i)):
            answer += 1
    return answer