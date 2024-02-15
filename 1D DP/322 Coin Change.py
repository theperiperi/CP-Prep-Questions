class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]+([float('inf')]*amount)
        for current_amount in range(1,amount+1):
            for coin in coins:
                if coin<=current_amount:
                    dp[current_amount]=min(dp[current_amount],dp[current_amount-coin]+1)
        if dp[-1]==float('inf'):
            return -1
        return dp[-1]
