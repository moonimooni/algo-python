# https://leetcode.com/problems/lemonade-change/description/

from typing import List


class Solution:
    FIVE, TEN, TWENTY = 5, 10, 20

    def lemonadeChange(self, bills: List[int]) -> bool:
        changes: dict[int, int] = {
            self.FIVE: 0,
            self.TEN: 0,
            self.TWENTY: 0
        }

        for bill in bills:
            self.__calculate_change(changes, bill)
            if any(change < 0 for change in changes.values()):
                return False

        return True

    def __calculate_change(self, changes: dict[int, int], bill: int):
        if bill == self.FIVE:
            changes[self.FIVE] += 1

        elif bill == self.TEN:
            changes[self.FIVE] -= 1
            changes[self.TEN] += 1

        elif bill == self.TWENTY:
            if changes[self.TEN] > 0:
                changes[self.TEN] -= 1
                changes[self.FIVE] -= 1
            else:
                changes[self.FIVE] -= 3
            changes[self.TWENTY] += 1

        return


s = Solution()
print(s.lemonadeChange([5, 5, 5, 10, 20]))
print(s.lemonadeChange([5, 5, 10, 10, 20]))
print(s.lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]))
