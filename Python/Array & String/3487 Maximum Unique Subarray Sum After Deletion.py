class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = list(set(nums))
        sumi =0

        if len(nums) == 1:
            return nums[0]

        for i in nums:
            if i > 0:
                sumi += i
                
        if sumi==0:
            return max(nums)
        return sumi
