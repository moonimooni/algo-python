# https://www.acmicpc.net/problem/2292

def comb(n):
    small, big, bigger = 1, 1, 0
    while True:
        if n >= small and n <= big:
            return (big // 6) - (small // 6) + 1
        else:
            small = big + 1
            bigger += 6
            big += bigger

print(comb(int(input())))