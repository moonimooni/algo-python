import time
start_time = time.time()

def two_sum(nums, target):

    # 아래 코드를 작성해주세요.

    # 투포인터
    # nums_ = sorted(nums)

    # i_1, i_2 = 0, len(nums)-1
    # while i_1 < i_2:
    #     if nums_[i_1] + nums_[i_2] < target:
    #         i_1 += 1
    #     elif nums_[i_1] + nums_[i_2] > target:
    #         i_2 -= 1
    #     elif nums_[i_1] + nums_[i_2] == target:
    #         return [i_1, i_2]
    # return None

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([4,9,11,14,10,20,30,50,40,33,46,88,29,41,16], 13))
print(f'걸린 시간: {(time.time() - start_time) * 10000}')
