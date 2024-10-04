class Solution:
    def rob(self, nums: list[int]) -> int:

        #if it is an array with one or to elements
        if len(nums)<3:
            return max(nums)

        #prev represents each value per cycle
        prev=nums[0]
        #curr represents max value
        curr=max(nums[0],nums[1])

        for n in range(2,len(nums)):
            curr,prev=max(curr,nums[n]+prev),curr
        return curr

        
