# https://leetcode.com/problems/count-primes/

# 에라토스테네스의_체

class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * 2 + [True] * (n-1)

        max_gcd = int(n ** 0.5)
        for i in range(2, max_gcd + 1):
            if sieve[i] == True:
                for j in range(i+i, n, i):
                    sieve[j] = False

        return len([i for i in range(n) if sieve[i] == True])


solution = Solution()
print(solution.countPrimes(10))
