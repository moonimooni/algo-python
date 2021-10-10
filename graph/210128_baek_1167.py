# https://www.acmicpc.net/problem/1167

import sys
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v+1)]
dims = list()

for i in range(v):
  edge = list(map(int, input().split()))[:-1]
  vertex = edge.pop(0)
  index = 0
  while index + 1 < len(edge):
    tree[vertex].append((edge[index],edge[index+1]))
    index += 2

w1 = [0 for _ in range(v+1)]

def dfs(start, weights):
  for node, distance in tree[start]:
    if weights[node] == 0:
      weights[node] += distance + weights[start]
      dfs(node, weights)

dfs(1, w1)
w1[1] = 0
v2 = w1.index(max(w1))
w2 = [0 for _ in range(v+1)]
dfs(v2, w2)
w2[v2] = 0
print(max(w2))


################################### 시간초과

# import sys
# input = sys.stdin.readline

# v = int(input())
# tree = [dict() for _ in range(v+1)]
# dims = list()

# for i in range(v):
#   edge = list(map(int, input().split()))[:-1]
#   vertex = edge.pop(0)
#   index = 0
#   while index + 1 < len(edge):
#     tree[vertex][edge[index]] = edge[index+1]
#     index += 2

# for j in range(v):
#   root = j + 1
#   stack = [root]
#   visited = [False for _ in range(v + 1)]
#   dim = 0
#   while stack:
#     node = stack.pop()
#     end = list(tree[node].keys())
#     if visited[node] == False:
#       visited[node] = True
#       if visited[end[-1]] == True:
#         dims.append(dim)
#         break
#       stack += end
#       dim += tree[node][stack[-1]]

# dims.sort(reverse=True)
# print(dims[0])