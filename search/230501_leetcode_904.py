# https://leetcode.com/problems/fruit-into-baskets/description/

from typing import List


class Solution:
    # 좌 포인터가 움직이는 시점은 :
    #   바구니 다 채웠을때
    # 우 포인터가 움직이는 시점은 :
    #   좌 포인터 옮지면 우 포인터도 좌 포인터 시점으로 리셋
    #   바구니 다 찰 때까지 우 포인터 이동

    def totalFruit(self, fruits: List[int]) -> int:
        maximum_fruits = 0
        fruit_varables = list()
        left_pointer, right_pointer = 0, 0

        while left_pointer < len(fruits):
            fruit_count = 0

            if fruits[right_pointer] in fruit_varables:
                fruit_count += 1
            else:
                if len(fruit_varables) == 2:
                    maximum_fruits = max(maximum_fruits, fruit_count)
                    fruit_count = 0
                    left_pointer += 1
                    right_pointer = left_pointer
                else:
                    fruit_varables.append(fruits[right_pointer])
                    fruit_count += 1

        return maximum_fruits
