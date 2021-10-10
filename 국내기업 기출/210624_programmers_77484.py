# 초기 풀이
def rank(win_count):
    if win_count == 6:
        return 1
    elif win_count == 5:
        return 2
    elif win_count == 4:
        return 3
    elif win_count == 3:
        return 4
    elif win_count == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    win = 0
    answer = []
    for l in lottos:
        if l in win_nums:
            win += 1
            win_nums.remove(l)
            
    zeroes = lottos.count(0)
    
    if len(win_nums) >= zeroes:
        answer += [rank(zeroes+win), rank(win)]
    else:
        answer += [rank(len(win_nums)+zeroes), rank(win)]
        
    return answer

# 수정

def solution(lottos, win_nums):
    rank, win = [6,6,5,4,3,2,1], 0
    
    answer = []
    
    for l in lottos:
        if l in win_nums:
            win += 1

    zeroes = lottos.count(0)
    return [rank[win+zeroes], rank[win]]