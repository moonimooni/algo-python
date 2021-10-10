# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    bucket = []
    
    for move in moves:
        for line in board:
            if line[move-1] != 0:
                bucket.append(line[move-1])
                line[move-1] = 0
                break

        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            answer += 2
            bucket = bucket[:-2]
            
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))