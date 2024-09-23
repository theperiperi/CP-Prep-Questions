class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary)
        n = len(s)
        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if sub in dict_set:
                    dp[i] = min(dp[i], dp[j])
            dp[i] = min(dp[i], dp[i - 1] + 1)

        return dp[n]
