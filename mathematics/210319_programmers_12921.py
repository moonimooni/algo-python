# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    nums = list(range(3, n+1, 2))
    if not nums:
        return answer + 1
    else:
        end = nums[-1]
        nums = set(nums)

    for i in range(3, end+1):
        if i in nums:
            nums -= set(range(i*2, end+1, i))

    answer += len(nums) + 1
    return answer