class Solution(object):
    def triangularSum(self, nums):
        n = len(nums)
        coeff = 1
        total = 0
        for i in range(n):
            # add contribution of nums[i]
            total += coeff * nums[i]
            # update coefficient for next i
            coeff = coeff * (n-1-i) // (i+1) if i < n-1 else 1
        return total % 10
