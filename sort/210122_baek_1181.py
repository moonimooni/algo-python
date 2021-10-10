# https://www.acmicpc.net/problem/1181


#################################################### 재귀 오류.. ㅠ

# import sys
# n = int(sys.stdin.readline())
# answer = [sys.stdin.readline().strip() for i in range(n)]

# def func(answer):
#     if len(answer) <= 1:
#         return answer
#     answer.sort()
#     pivot = answer[0]
#     left = [word for word in answer[1:] if len(word) < len(pivot) and word != pivot]
#     right = [word for word in answer[1:] if len(word) >= len(pivot) and word != pivot]
#     left.sort()
#     right.sort()
#     return func(left) + [pivot] + func(right)
  
# print(func(answer))

#################################################################

# import sys

# n = int(sys.stdin.readline())
# words = []
# for _ in range(n):
#   a = sys.stdin.readline().strip()
#   b = len(a)
#   if (a,b) in words:
#     continue
#   words.append((a,b))

# words.sort(key = lambda x: x[0])
# words.sort(key = lambda x: x[1])

# for word in words:
#   print(word[0])

##################################################################

import sys
input = sys.stdin.readline

words = list(set(input().strip() for i in range(int(input()))))
words.sort(key = lambda x: (len(x), x))

print(*words, sep='\n')