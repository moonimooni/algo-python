# https://leetcode.com/problems/max-area-of-island/description/

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        row_len, col_len = len(grid), len(grid[0])

        for row in range(row_len):
            for col in range(col_len):
                area = self.__dfs(grid, row, col)
                answer = area if area > answer else answer

        return answer

    def __dfs(self, grid, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
            grid[row][col] = 0
            return \
                self.__dfs(grid, row+1, col) + \
                self.__dfs(grid, row, col+1) + \
                self.__dfs(grid, row-1, col) + \
                self.__dfs(grid, row, col-1) + 1

        return 0


s = Solution()
# s.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]])
print(s.maxAreaOfIsland(grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
# print(s.maxAreaOfIsland(
#     [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
