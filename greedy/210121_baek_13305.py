# https://www.acmicpc.net/problem/13305

import sys

n = int(sys.stdin.readline())
km = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

def func(roads, cities):
  answer = 0
  cheapest = min(cities)
  left_km = sum(roads)
  dep, dest = 0, 1

  while left_km > 0:
    if cities[dep] == cheapest:
      answer += (left_km * cheapest)
      return answer
    while cities[dep] <= cities[dest]:
      dest += 1
    to_go = sum(roads[dep:dest])
    answer += (cities[dep] * to_go)
    left_km -= to_go
    dep = dest
    dest += 1
  return answer

print(func(km, cost))

# 다른사람 풀이

# import sys

# input = sys.stdin.readline

# n = int(input())
# dist = list(map(int, input().split()))
# price = list(map(int, input().split()))

# cost = price[0]*dist[0]
# min_p = price[0]
# for i in range(1, len(price) - 1):
#     min_p = min(min_p, price[i])
#     cost += min_p*dist[i]

# print(cost)