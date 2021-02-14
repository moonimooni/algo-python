# https://www.acmicpc.net/problem/2231

n = int(input())

min = n
for _ in str(n):
    min -= 9
    if min <= 0:
        min = 1
        break
for num in range(min, n):
    if num + sum([int(i) for i in str(num)]) == n:
        print(num)
        exit(0)
print(0)