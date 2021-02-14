# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

arr = [1, 5, 2, 6, 3, 7, 4]
cmd = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(arr, cmd))

### 다른 사람 풀이

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))