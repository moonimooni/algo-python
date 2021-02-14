# https://www.acmicpc.net/problem/1260

n, m, v = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
  node1, node2 = map(int, input().split())
  graph[node1][node2] = 1
  graph[node2][node1] = 1

def dfs(v, dfs_visited):
  dfs_visited += [v]
  for n in range(len(graph[v])):
    if graph[v][n] != 0 and n not in dfs_visited:
      dfs(n, dfs_visited)
  return dfs_visited

def bfs(v):
  bfs_visited, bfs_q = [v], [v]
  while bfs_q:
    node = bfs_q.pop(0)
    for n in range(len(graph[node])):
      if graph[node][n] != 0 and n not in bfs_visited:
        bfs_q.append(n)
        bfs_visited.append(n)
  return bfs_visited

print(*dfs(v, []))
print(*bfs(v))