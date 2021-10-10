# https://www.acmicpc.net/problem/18258

import sys
input = sys.stdin.readline
from collections import deque
q = deque([])

for _ in range(int(input())):
  cmd = input().split()
  if cmd[0] == 'push':
    q.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if not q:
      print(-1)
    else:
      print(q.popleft())
  elif cmd[0] == 'size':
    print(len(q))
  elif cmd[0] == 'empty':
    if not q:
      print(1)
    else:
      print(0)
  elif cmd[0] == 'front':
    if not q:
      print(-1)
    else:
      print(q[0])
  elif cmd[0] == 'back':
    if not q:
      print(-1)
    else:
      print(q[-1])