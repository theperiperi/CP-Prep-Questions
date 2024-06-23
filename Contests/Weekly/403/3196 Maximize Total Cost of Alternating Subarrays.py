class Solution:
    def max_total_cost(self, dp, nums, index, include_last):
        if index < 0:
            return 0
        if index == 0:
            if include_last == 0:
                return nums[0]
            else:
                return -float('inf')
        if dp[index][include_last] != -1:
            return dp[index][include_last]
        
        max_cost = -float('inf')
        
        if include_last == 0:
            max_cost = max(max_cost, nums[index] + self.max_total_cost(dp, nums, index - 1, 0))
            max_cost = max(max_cost, nums[index] + self.max_total_cost(dp, nums, index - 1, 1))
        elif include_last == 1:
            max_cost = max(max_cost, -nums[index] + self.max_total_cost(dp, nums, index - 1, 0))
        
        dp[index][include_last] = max_cost
        return max_cost

    def maximumTotalCost(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [[-1] * 2 for _ in range(n)]
        
        max_cost = -float('inf')
        for include_last in range(2):  
            max_cost = max(max_cost, self.max_total_cost(dp, nums, n - 1, include_last))
        
        return max_cost
