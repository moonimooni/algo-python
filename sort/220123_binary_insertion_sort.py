import random


def binary_search(numbers, target, start, end):
    # 예를 들어 0, 1 인덱스를 비교할 때
    # 0 인덱스가 target보다 크면 target이 그자리로 가야함
    if start == end:
        return start if numbers[start] > target else start + 1

    # 일반적인 binary search였다면 return -1 or return False
    # 하지만 insertion sort에 사용되기 때문에 return start
    if start > end:
        return start

    mid = (start + end) // 2
    if numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        return binary_search(numbers, target, start, mid - 1)
    else:
        return binary_search(numbers, target, mid + 1, end)


def binary_insertion_sort(numbers):
    for i in range(1, len(numbers)):
        target = numbers[i]
        j = binary_search(numbers, target, 0, i - 1)
        numbers = numbers[:j] + [target] + numbers[j:i] + numbers[i + 1:]
    return numbers


numbers = [random.randint(0, 100) for _ in range(30)]
print(numbers)
print(binary_insertion_sort(numbers))
