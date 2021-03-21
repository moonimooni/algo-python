# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    keypad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    left_p, right_p = (0, 3), (2, 3)

    for num in numbers:
        if num in keypad[0]:
            answer += 'L'
            left_p = (0, keypad[0].index(num))
        elif num in keypad[2]:
            answer += 'R'
            right_p = (2, keypad[2].index(num))
        else:
            left, right = bool(hand == 'left'), bool(hand == 'right')
            position = (1, keypad[1].index(num)) #(1,1)
            left_far = abs(left_p[0] - position[0]) + abs(left_p[1] - position[1]) #(0,1)
            right_far = abs(right_p[0] - position[0]) + abs(right_p[1] - position[1]) #(2,0)
            
            if left_far > right_far:
                left, right = False, True
            elif left_far < right_far:
                left, right = True, False
            
            if left:
                answer += 'L'
                left_p = (1, keypad[1].index(num))
            else:
                answer += 'R'
                right_p = (1, keypad[1].index(num))
    
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))