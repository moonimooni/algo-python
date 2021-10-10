# https://www.acmicpc.net/problem/10799

line = list(input())
bars = 0
stack = []

for i in range(len(line)):
  if line[i] == '(':
    stack.append('(')
    bars += 1
  if line[i] == ')':
    stack.pop()
    if line[i-1] == '(':
      bars -= 1
      bars += len(stack)
print(bars)