# https://programmers.co.kr/learn/courses/30/lessons/12913

# 문제 설명
# 땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

# 예를 들면,

# | 1 | 2 | 3 | 5 |

# | 5 | 6 | 7 | 8 |

# | 4 | 3 | 2 | 1 |

# 로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.

# 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요. 위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.

# ---------------------------------

# 열은 4개로 한정되어 있다.
# 각 인덱스가 출발점이 된다.
# 아래 행으로 내려가면서 같은 인덱스가 아닌 값 중 가장 큰 값을 더해준다.


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = max(land[i-1][:j] + land[i-1][j+1:]) + land[i][j]
    return max(land[-1])


# scores = list()


# def dfs(i, j, land, score=0):
#     MAX_ROW = len(land)
#     MAX_COL = 4

#     if i >= MAX_ROW or i < 0 or j >= MAX_COL or j < 0:
#         return False

#     score += land[i][j]

#     if i == MAX_ROW-1:
#         scores.append(score)

#     for _j in range(MAX_COL):
#         if (j != _j):
#             dfs(i+1, _j, land, score)

#     return scores


# def solution(land):
#     MAX_ROW = len(land)
#     MAX_COL = 4
#     scores = list()
#     for i in range(MAX_ROW):
#         for j in range(MAX_COL):
#             result = dfs(i, j, land)
#             if (result):
#                 scores += result

#     return max(scores)


print(solution([[100, 1, 0, 2], [900, 30, 1, 10]]))
