# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    n, m = min(n, m), max(n, m)
    
    for i in range(n,0,-1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    answer.append((n // answer[0]) * (m // answer[0]) * answer[0])
    return answer

print(solution(9, 12))