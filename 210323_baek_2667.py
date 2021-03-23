# https://www.acmicpc.net/problem/2667

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input())))

answer, cnt = [0], 0

def dfs(i, j):
    global cnt
    
    if i >= n or i < 0 or j >= n or j < 0:
        return False
    if matrix[i][j] == 0:
        return False

    matrix[i][j] = 0
    cnt += 1

    dfs(i+1,j)
    dfs(i,j+1)
    dfs(i-1,j)
    dfs(i,j-1)

    return True

for i in range(n):
    for j in range(n):
        search = dfs(i,j)
        if search:
            answer[0] += 1
            answer.append(cnt)
            cnt = 0

answer = answer[:1] + sorted(answer[1:])

print(*answer, sep='\n')