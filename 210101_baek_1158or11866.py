# https://www.acmicpc.net/problem/1158

# qtt, turn = map(int, input().split())
# turn -= 1
# i = turn
# alive = [i for i in range(1, qtt+1)]
# answer = '<'

# while len(alive) != 0:
#   while i >= len(alive):
#     i -= len(alive)
#   answer += str(alive[i]) + ', '
#   alive.pop(i)
#   i += turn
# answer = answer[:len(answer)-2] + '>'

# print(answer)

def josephus(n, k):
  survivors = [i for i in range(1, n + 1)]
  answer = '<'
  k -= 1
  target_i = k
  while survivors:
    while target_i >= len(survivors):
      target_i -=len(survivors)
    target = survivors.pop(target_i)
    answer += str(target) + ', '
    target_i += k
  answer = answer[:-2] + '>'
  return answer

a, b = map(int, input().split())

print(josephus(a, b))