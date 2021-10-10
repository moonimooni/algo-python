# https://programmers.co.kr/learn/courses/30/lessons/12977

# 소수 만들기

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