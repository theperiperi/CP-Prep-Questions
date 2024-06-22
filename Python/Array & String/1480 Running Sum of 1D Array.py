class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        for i in range(len(nums)):
            count+=nums[i]
            nums[i]=count
        return nums

        
