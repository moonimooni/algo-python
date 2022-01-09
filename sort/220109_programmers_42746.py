# https://programmers.co.kr/learn/courses/30/lessons/42746

# from itertools import permutations


# 시간 초과.. obviously
# def solution(numbers):
# numbers = list(map(str, numbers))
# permutation_result = permutations(numbers)
# numbers_in_string = [''.join(el) for el in permutation_result]
# return sorted(numbers_in_string)[-1]


# what if... sort by element's index value in order?
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x[-1::-1][0], reverse=True)
#     return str(int(''.join(numbers)))


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


print(solution([9, 5, 34, 30, 3]))
