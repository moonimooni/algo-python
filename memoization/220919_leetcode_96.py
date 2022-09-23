# https://leetcode.com/problems/unique-binary-search-trees/
# 1부터 n까지의 node로 유니크한 바이너리 트리 가지수를 구하여라.
# for n, for j (j < n)

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1, 2] + [0] * (n - 2)
        if n <= 2:
            return dp[n]
        for i in range(3, n+1):
            for j in range(i): 
                dp[i] += dp[j] * dp[i-1-j]
                # if i = 4, dp[4] = (dp[0] * dp[3]) + (dp[1] * dp[2]) + (dp[2] * dp[1]) + (dp[3] * dp[0])
        return dp[n]
