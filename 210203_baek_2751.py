# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

a = list()
n = int(input())
for _ in range(n):
    a.append(int(input()))

a.sort()
for num in a:
    print(num)

########################### 메모리.. ㅠ
# def q_sort(arr):
#   if len(arr) <= 1:
#     return arr
#   pivot = arr[0]
#   left, right = list(), list()
#   for num in arr[1:]:
#     if num > pivot:
#       right.append(num)
#     else:
#       left.append(num)
#   return q_sort(left) + [pivot] + q_sort(right)

# print(*q_sort(a), sep='\n')
