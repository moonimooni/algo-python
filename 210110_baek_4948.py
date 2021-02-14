# https://www.acmicpc.net/problem/4948

import math

answer = []
sieve = ['prime'] * (123456 * 2 + 1)
max_sub_n = math.ceil(math.sqrt(123456 * 2 + 1))

for i in range(2, max_sub_n):
    if sieve[i] == 'prime':
        for j in range(i*2, len(sieve), i):
            sieve[j] = j

def bertrands(min_n):
    cnt = 0
    for i in range(min_n+1, min_n * 2+1):
        if sieve[i] == 'prime':
            cnt += 1
    answer.append(cnt)

while True:
    num = int(input())
    if num == 0:
        break
    bertrands(num)

print(*answer, sep='\n')