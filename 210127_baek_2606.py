# https://www.acmicpc.net/problem/2606


coms = int(input())
edges = list()

for _ in range(int(input())):
    edges.append(tuple(map(int, input().split())))

graph = [[] for _ in range(coms+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
q = [1]
answer = [False for _ in range(coms+1)]
while q:
    p = q.pop(0)
    if answer[p] == False:
        answer[p] = True
        q += graph[p]
answer = list(filter(lambda x: x == True, answer))

print(len(answer)-1)