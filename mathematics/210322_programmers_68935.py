# https://programmers.co.kr/learn/courses/30/lessons/68935

# 파이썬이 사기다 ;; 3진법 계산 내장 함수가 있다니

def solution(n):
    n3 = ''
    while n:
        n, r = divmod(n, 3)
        n3 += str(r)
    return int(n3, 3)

print(solution(125))