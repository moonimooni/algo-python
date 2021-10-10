# https://www.acmicpc.net/problem/2750

total = int(input())
answer = list()

for i in range(total):
  add = int(input())
  answer.append(add)

for j in range(len(answer)-1):
  for k in range(len(answer)-1-j):
    if answer[k] > answer[k+1]:
      answer[k], answer[k+1] = answer[k+1], answer[k]

print(*answer, sep='\n')