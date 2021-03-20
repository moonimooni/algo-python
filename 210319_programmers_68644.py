from itertools import combinations

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    # pairs = combinations(numbers, 2)
    # for pair in pairs:
    #     answer.append(sum(pair))
    
    return sorted(list(set(answer)))
            
    return answer