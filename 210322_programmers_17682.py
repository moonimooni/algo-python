# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    sqrt = {'S':1, 'D':2, 'T':3}
    cut = []

    for i in range(1, len(dartResult)):
        if dartResult[i] == '#' or dartResult[i] == '*':
            cut.append(i+1)
        elif dartResult[i] in sqrt.keys() and dartResult[i+1].isnumeric():
            cut.append(i+1)
        if len(cut) == 2:
            break

    results = [dartResult[:cut[0]], dartResult[cut[0]:cut[1]], dartResult[cut[1]:]]
    scores = [0, 0, 0]

    fever = 0
    for i, result in enumerate(results):
        scr = 0
        for j in range(len(result)):
            if not result[j].isnumeric():
                scores[i] += int(result[:j])**sqrt[result[j]]
                break

        if result[-1] == '#':
            scores[i] *= -1
        elif result[-1] == '*':
            if i != 0:
                scores[i-1] *= 2
            scores[i] *= 2
            fever += 1

    return sum(scores)

print(solution('10D10S*0S'))