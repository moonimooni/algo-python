# https://programmers.co.kr/learn/courses/30/lessons/42862

# 문제 설명
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

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