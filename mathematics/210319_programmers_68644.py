# 조합
# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    pairs = combinations(numbers, 2)
    return sorted(list(set([sum(pair) for pair in pairs])))

# 아래는 js
# function solution(numbers) {
#     const answer = [];
#     for (let i=0; i<numbers.length; i++) {
#         for (let j=i+1; j<numbers.length; j++) {
#             const sumNum = numbers[i]+numbers[j]
#             if (!answer.includes(sumNum)) {
#                 answer.push(sumNum)
#             }
#         }
#     }
#     answer.sort((a,b) => a-b);
#     return answer
# }