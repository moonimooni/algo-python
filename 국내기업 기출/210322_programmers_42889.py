# https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter

def solution(N, stages):
    answer = [[i,0] for i in range(N+1)]
    check = Counter(stages)

    for stage in range(1,N+1):
        if stage in check.keys():
            passed = sum([val for key, val in check.items() if key >= stage])
            answer[stage][1] += (check[stage]/passed)

    answer = sorted(answer[1:], key=lambda x:x[1], reverse=True)
    answer = list(map(lambda x: x[0], answer))            
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))