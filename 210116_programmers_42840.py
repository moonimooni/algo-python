# https://programmers.co.kr/learn/courses/30/lessons/42840

# def solution(answers):

#     p1 = [1, 2, 3, 4, 5]
#     p2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     p1_cor, p2_cor, p3_cor = 0, 0, 0
#     p1_loop, p2_loop, p3_loop = 0, 0, 0

#     for i in answers:
#         if p1[p1_loop] == i:
#             p1_cor += 1
#         p1_loop += 1
#         if p1_loop == 5:
#             p1_loop = 0

#         if p2[p2_loop] == i:
#             p2_cor += 1
#         p2_loop += 1
#         if p2_loop == 8:
#             p2_loop = 0

#         if p3[p3_loop] == i:
#             p3_cor += 1
#         p3_loop += 1
#         if p3_loop == 10:
#             p3_loop = 0

#     scores = [p1_cor, p2_cor, p3_cor]
#     winner_score = max(scores)
#     answer = [i+1 for i in range(len(scores)) if scores[i] == winner_score]
#     return answer

# enumerate 를 활용할 수도.

from itertools import cycle

def solution2(answers):
    friends = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]

    scores = [0, 0, 0]

    for i in answers:
        for j in range(len(friends)):
            if i == next(friends[j]):
                scores[j] += 1
    
    answer = [k+1 for k in range(len(scores)) if scores[k] == max(scores)]
    return answer