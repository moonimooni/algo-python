#https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer = str(n % 3) + answer
            n //= 3
        else:
            answer = "4" + answer
            n = n//3 - 1
    return answer
