def solution(N):
    binary = bin(N)[2:]

    cnt = 0
    cdd = []

    for b in binary:
        if b == '0':
            cnt += 1
            continue

        cdd.append(cnt)
        cnt = 0

    return max(cdd)