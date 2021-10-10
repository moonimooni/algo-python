# https://www.acmicpc.net/problem/9184

cach = [[[0]*21 for i in range(21)] for j in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        a, b, c = 20, 20, 20
    if cach[a][b][c] == 0:
        if a < b and b < c:
            cach[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            cach[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return cach[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
      break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')

################################################ 비슷한 다른 풀이

# cach = dict()

# def w(a, b, c):
#     if (a, b, c) not in cach.keys():
#         if a <= 0 or b <= 0 or c <= 0:
#             return 1
#         if a > 20 or b > 20 or c > 20:
#             a, b, c = 20, 20, 20
#         if a < b and b < c:
#             cach[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#         else:
#             cach[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
#     return cach[(a, b, c)]

# while True:
#     a, b, c = map(int, input().split())
#     if a == -1 and b == -1 and c == -1:
#         break
#     print(f'w({a}, {b}, {c}) = {w(a, b, c)}')