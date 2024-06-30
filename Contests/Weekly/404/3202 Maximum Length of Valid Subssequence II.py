class Solution(object):
    def maximumLength(self, nums,k):
        # DP array to store lengths of valid subsequences
        dp = [0] * (k * k)
        
        def helper(x, y, k):
            # Map the (x, y) pair to a unique index
            return x * k + y
        
        for num in nums:
            # Get the current remainder of the number
            num %= k
            # Update the DP table for all possible remainders
            for i in range(k):
                if dp[helper(num, i, k)] + 1 > dp[helper(i, num, k)]:
                    dp[helper(i, num, k)] = dp[helper(num, i, k)] + 1
        
        # Return the maximum value in the DP table
        return max(dp)
