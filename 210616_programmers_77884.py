def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if num == 1:
            divisor_count = 1
        else:
            divisor_count = 2

        maximum = num // 2

        for i in range(2, maximum+1):
            if not num % i:
                divisor_count += 1
                
        if divisor_count % 2:
            answer -= num
        else:
            answer += num
    return answer

# 다른 사람 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(1,1000))