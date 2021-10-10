# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) >= 2:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        else:
            break
        answer += 1

    if scoville[0] >= K:
        return answer
    else:
        return -1


scoville = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(scoville, k))
