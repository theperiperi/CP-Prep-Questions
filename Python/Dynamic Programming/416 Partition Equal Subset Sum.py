class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total%2==1:
            return False
        k= total //2

        def function(i, total):
            if total == k:
                return True
            if i<0 or total>k:
                return False
            return function(i-1, total+nums[i]) or function(i-1,total)
        return function(len(nums) - 1, 0)
