class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        mod = 10**9 + 7
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            val = i**x
            if val > n:
                break
            for j in range(n, val-1, -1):
                dp[j] = (dp[j] + dp[j-val]) % mod

        return dp[n]
