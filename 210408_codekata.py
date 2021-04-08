from collections import Counter

def top_k(nums, k):
    count = Counter(nums)
    count = sorted(count, key=count.get, reverse=True)
    return count[:k]

print(top_k([1,1,2,2,2,2,3,3,3], 2))