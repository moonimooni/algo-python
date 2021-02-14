A = list(map(int, input().split()))

def scale(array):
    ascending = 0
    descending = 0
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            descending += 1
        elif array[i-1] < array[i]:
            ascending += 1
        if ascending != 0 and descending != 0:
            return 'mixed'
    if descending == 0:
        return 'ascending'
    elif ascending == 0:
        return 'descending'

print(scale(A))