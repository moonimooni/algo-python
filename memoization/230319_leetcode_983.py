# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 날짜별 가격 dp, value는 0으로 init
        costs_by_days = [0] * (days[-1] + 1)

        for day in range(1, len(costs_by_days)):
            # 구매하는 날에 해당하지 않는다면, 그 전날 비용과 동일
            if day not in days:
                costs_by_days[day] = costs_by_days[day-1]
            else:
                # 1,7,30일 전에 해당 티켓을 샀을때 무엇이 최저가인지 비교.
                one_day_pass, seven_day_pass, one_month_pass = \
                    costs_by_days[day-1 if day-1 > 0 else 0] + costs[0], \
                    costs_by_days[day-7 if day-7 > 0 else 0] + costs[1], \
                    costs_by_days[day-30 if day-30 > 0 else 0] + costs[2]

                costs_by_days[day] = min(one_day_pass, seven_day_pass, one_month_pass)

        return costs_by_days[-1]


s = Solution()
print(s.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
print(s.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
