# https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    answer = []
    required_days = [math.ceil((100 - p)/s)
                     for p, s in zip(progresses, speeds)]
    criteria = 0
    for i in range(criteria+1, len(progresses)):
        if required_days[criteria] < required_days[i]:
            answer.append(i-criteria)
            criteria = i
    answer.append(len(progresses[criteria:]))
    return answer

# p = [93, 30, 55]
# s = [1, 30, 5]

p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]

print(solution(p, s))
