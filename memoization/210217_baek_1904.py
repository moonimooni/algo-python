# https://www.acmicpc.net/problem/1904

# t1, t2 = '00', '1'

# cache = dict()
# cache[1] = 1
# cache[2] = 2
# cache[3] = 3
# cache[4] = 5
# cache[5] = 8
# cache[6] = 13
# cache[7] = 21

n = int(input())
cache = dict()
cache[1], cache[2] = 1, 2
for i in range(3, n+1):
    cache[i] = (cache[i-2] + cache[i-1]) % 15746
print(cache[n])

# 아래 코드가 더 빠르다.. 왜?

N = int(input())
cache = [0, 1, 2]
for _ in range(3, N+1):
    cache.append((cache[-1]+cache[-2]) % 15746)
print(cache[N])

# 시간초과

# n = int(input())
# a, b = 1, 2
# for i in range(n-1):
#     a, b = b, a + b
# print(a % 15746)

import sys

maximum = sys.maxsize