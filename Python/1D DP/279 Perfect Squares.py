class Solution:
    def numSquares(self, n: int) -> int:
        dp = [20000 for _ in range(n + 1)]
        dp[0] = 0
        ps = []

        for i in range(1,n + 1):
            if pow(i, 2) > n:
                break
            ps.append(i ** 2)

        for i in range(n + 1):
            for j in ps:
                if i + j <= n:
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
                else:
                    break

        return dp[n]
