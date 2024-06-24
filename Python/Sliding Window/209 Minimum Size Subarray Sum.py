class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minimum_value=9999999
        suma=0
        left=0
        right=0

        for right in range(len(nums)):
            suma+=nums[right]

            while suma>=target:
                minimum_value=min(minimum_value,right-left+1)
                suma-=nums[left]
                left+=1
        
        if minimum_value==9999999:
            return 0
        return minimum_value
