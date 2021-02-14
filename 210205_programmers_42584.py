# https://programmers.co.kr/learn/courses/30/lessons/42584

import sys
input = sys.stdin.readline

def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    for i in range(1, len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            dropped = stack.pop()
            answer[dropped] += i - dropped
        stack.append(i)

    while stack:
        time = stack.pop()
        answer[time] += len(prices) - time - 1
    
    return answer


# prices = [1, 2, 3, 2, 3]
prices = [3, 2, 2, 4, 1]

print(solution(prices))