import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque([i+1 for i in range(n)])

def card(num, arr):
  while len(arr) != 1:
    arr.popleft()
    switch = arr.popleft()
    arr.append(switch)
  return arr[0]

print(card(n, q))