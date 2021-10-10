# https://www.acmicpc.net/problem/10250

def func(h, w, n):
  flr, rm = None, None
  
  if (n % h) == 0:
    flr = str(h)
    if n // h < 10:
      rm = str(0) + str(n // h)
    else :
      rm = str(n // h)
  else:
    flr = str(n % h)
    if n // h + 1 < 10:
      rm = str(0) + str(n // h + 1)
    else:
      rm = str(n // h + 1)

  return int(flr + rm)

for _ in range(int(input())):
  h, w, n = map(int, input().split())
  print(func(h, w, n))