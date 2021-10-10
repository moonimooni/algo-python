def move_zeroes(nums):
    zeroes = nums.count(0)

    i = 0
    count = zeroes
    while i < len(nums) and count:
        if nums[i] == 0:
            nums.pop(i)
            count -= 1
        else:
            i += 1

    for z in range(zeroes):
        nums.append(0)
    
    return nums

print(move_zeroes([0,2,0,3,5]))