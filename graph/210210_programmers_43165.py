# https://programmers.co.kr/learn/courses/30/lessons/43165
answer = 0

def dfs(numbers, target, index, sum):
    global answer
    if index == len(numbers):
        if sum == target:
            answer += 1
            return
        else:
            return
    else:
        dfs(numbers, target, index+1, sum+numbers[index])
        dfs(numbers, target, index+1, sum-numbers[index])

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))