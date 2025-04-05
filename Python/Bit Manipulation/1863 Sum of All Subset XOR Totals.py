class Solution:
    def subsetXORSum(self, nums):
        total = 0
        for num in nums:
            total |= num
        return total * (1 << (len(nums) - 1))
