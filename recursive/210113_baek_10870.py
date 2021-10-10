# https://www.acmicpc.net/problem/10870

def fibo(integer):
  if integer == 0:
    return 0
  if integer == 1:
    return 1
  return fibo(integer-1) + fibo(integer-2)

print(fibo(int(input())))