# https://programmers.co.kr/learn/courses/30/lessons/42862

# def solution(n, lost, reserve):
#     robbed = list(set(lost) - set(reserve))
#     saviors = list(set(reserve) - set(lost))
#     answer = n - len(robbed)

#     for savior in saviors:
#         if len(robbed) == 0:
#             break

#         if savior - 1 in robbed:
#             robbed.remove(savior - 1)
#         elif savior + 1 in robbed:
#             robbed.remove(savior + 1)
#         else:
#             continue
#         answer += 1

#     return answer

# 10명 중 1,3,5,7 reserve = 4,6,8
# 10명 중 2,3,5,6,7,8 reserve = 1,2,4,9
# 10명 중 3,5,6,7,10 reserve = 2,6,8,9


# 다른사람 풀이.. O(n)으로 해결하는 법

def solution(n, lost, reserve):
    mates = [1 for i in range(n)]
    for l in lost:
        mates[l-1] -= 1
    for r in reserve:
        mates[r-1] += 1
    for i in range(len(mates)):
        if mates[i] == 0:
            if i+1 < len(mates) and mates[i+1] == 2:
                mates[i] += 1
                mates[i+1] -= 1
            elif i-1 >= 0 and mates[i-1] == 2:
                mates[i] += 1
                mates[i-1] -= 1
    answer = len([i for i in mates if i >= 1])
    return answer

print(solution(10, [3,5,6,7,10], [2,6,8,9]))