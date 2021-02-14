# https://www.acmicpc.net/problem/2110

#####################################################시간초과
# import sys

# n, c = map(int, input().split())

# houses = [int(sys.stdin.readline()) for i in range(n)]
# houses.sort()

# def setup(houses, wifi):
#   start, end = 1, houses[-1] - houses[0]
#   mid = (start + end) // 2
#   while mid >= start:
#     target = houses[0]
#     cnt = 1
#     for i in range(1, len(houses)):
#       if houses[i] - target >= mid:
#         target = houses[i]
#         cnt += 1
#     if cnt < wifi:
#       mid -= 1
#     if cnt > wifi:
#       mid += 1
#     if cnt == wifi:
#       return mid

# print(setup(houses, c))
#############################################################

import sys

n, c = map(int, input().split())

houses = [int(sys.stdin.readline()) for i in range(n)]
houses.sort()

def setup(houses, wifi):
  start, end = 1, houses[-1] - houses[0]
  while start <= end:
    mid = (start + end) // 2
    target = houses[0]
    cnt = 1
    for i in range(1, len(houses)):
      if houses[i] - target >= mid:
        target = houses[i]
        cnt += 1
    if cnt < wifi:
      end = mid - 1
    else :
      start = mid + 1
      answer = mid
  return answer

print(setup(houses, c))