class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max=0
        overall_max=-100000000000000000000000
        for num in nums:
            current_max=max(current_max+num,num)
            overall_max=max(overall_max,current_max)

        return overall_max        
