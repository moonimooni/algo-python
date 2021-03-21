# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = [x] * n
    return list(map(lambda a: a[1] + (a[0]*a[1]), enumerate(answer)))

print(solution(2, 5))