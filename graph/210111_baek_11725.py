# https://www.acmicpc.net/problem/11725


#############################################
# 메모리초과 ~

# import collections
# nodes_ttl = int(input())

# graph = [[0]*(nodes_ttl+1) for _ in range(nodes_ttl+1)]

# for _ in range(nodes_ttl-1):
#     insert = list(map(int, input().split()))
#     graph[insert[0]][insert[1]] = 1
#     graph[insert[1]][insert[0]] = 1

# vertices = dict()


# def find_parent(node):
#     vertices[node] = [0, []]
#     for i in range(nodes_ttl+1):
#         if graph[node][i] == 1:
#             if i in vertices:
#                 vertices[node][0] += i
#             else:
#                 vertices[node][1].append(i)
#                 find_parent(i)
#     return


# find_parent(1)

# for i in range(2, nodes_ttl+1):
#     print(vertices[i][0])

#############################################
# 시간초과 ~

# loop = int(input())

# found_parent = set([1])
# parent_info = dict()

# for i in range(loop - 1):
#   edge = list(map(int, input().split()))
#   if edge[0] in found_parent:
#     parent_info[edge[1]] = edge[0]
#     found_parent.add(edge[1])
#   else:
#     parent_info[edge[0]] = edge[1]
#     found_parent.add(edge[0])

# for j in range(2, loop + 1):
#   print(parent_info[j])

###################################################

nodes_ttl = int(input())
graph = [[] for _ in range(nodes_ttl + 1)]

for i in range(nodes_ttl-1):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

def find_parent(tree):
  answer = [0] * (nodes_ttl + 1)
  answer[1] = 1
  queue = [1]

  while queue:
    parent = queue.pop(0)
    for node in graph[parent]:
      if answer[node] == 0:
        answer[node] = parent
        queue.append(node)
  return answer

print(*find_parent(graph)[2:], sep='\n')

################################################