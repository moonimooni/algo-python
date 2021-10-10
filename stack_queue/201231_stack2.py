loop = int(input())
stack = []
answer = []

while loop:
  command = input().split()
  if command[0] == 'push':
    stack.append(int(command[1]))
  if command[0] == 'pop':
    if len(stack) > 0:
      popped = stack.pop()
      answer.append(popped)
    else:
      answer.append(-1)
  if command[0] == 'size':
    answer.append(len(stack))
  if command[0] == 'empty':
    if len(stack) == 0:
      answer.append(1)
    else:
      answer.append(0)
  if command[0] == 'top':
    if len(stack) == 0:
      answer.append(-1)
    else:
      answer.append(stack[-1])
  loop -= 1
print(*answer, sep='\n')