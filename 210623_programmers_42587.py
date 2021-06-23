from collections import deque

# 테스트케이스 일부 통과 실패 ㅠ


def solution(priorities, location):
    turn = 0
    dq = deque(priorities)

    while dq:
        if dq[0] != max(dq):
            popped = dq.popleft()
            dq.append(popped)

        elif dq[0] == max(dq):
            dq.popleft()
            turn += 1
            if location == 0:
                return turn

        if location > 0:
            location -= 1
            continue

        if location <= 0:
            location = len(dq) - 1

    return turn

# 다른사람 풀이


def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


print(f'answer is ! {solution([1, 2, 1, 2, 3, 9, 6, 1], 2)}')
