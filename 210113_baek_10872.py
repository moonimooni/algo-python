# https://www.acmicpc.net/problem/10872

def factorial(integer):
  if integer == 0:
    return 1
  if integer == 1:
    return 1
  return integer * factorial(integer-1)

print(factorial(int(input())))