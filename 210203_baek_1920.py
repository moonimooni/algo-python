# https://www.acmicpc.net/problem/1920


## 정통 풀이법

# N=int(input())
# A=list(map(int,input().split()))
# M=int(input())
# B=list(map(int,input().split()))
# A.sort()

# def search(target,list):
#     start=0
#     end=len(list)-1
#     while start<=end:
#         mid=(start+end)//2
#         if list[mid]==target: 
#           return 1
#         elif list[mid]<target: 
#           start=mid+1
#         else: end=mid-1
#     return 0

# for target in B:
#     print(search(target,A))

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

info = defaultdict(bool)
for a_num in a:
  info[a_num] = True

for b_num in b:
  if info[b_num] == True:
    print(1)
  else:
    print(0)

##### set 로 풀면 더 야매스럽게 풀 수 있다!

#################################시간초과
# def srch(num, array):
#     mid = len(array) // 2
#     if num > array[-1] or num < array[0]:
#         return 0
#     if len(array) == 1 and array[0] != num:
#         return 0
#     if array[mid] == num:
#         return 1
#     elif array[mid] > num:
#         return srch(num, array[:mid])
#     elif array[mid] < num:
#         return srch(num, array[mid:])

# a.sort()
# for num in b:
#     print(srch(num, a))

