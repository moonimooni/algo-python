# https://www.acmicpc.net/problem/2775

t = int(input())

for _ in range(t):
  flr = int(input())
  rm = int(input())
  ans = [i for i in range(rm+1)]
  for i in range(flr):
    for j in range(2, rm+1):
      ans[j] += ans[j-1]
  print(ans[-1])

# recursive call (inefficient)

# t = int(input())

# def recursive(flrs, rms):
#   ppl = 0
#   if flrs == 0:
#     return rms
#   for rm in range(1, rms+1):
#     ppl += recursive(flrs-1, rm)
#   return ppl

# for _ in range(t):
#   flr = int(input())
#   rm = int(input())
#   print(recursive(flr, rm))