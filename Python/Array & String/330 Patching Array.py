class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ans=0
        sum=0
        i=0
        while sum<n:
            if i<len(nums) and nums[i]<=sum+1:
                sum+=nums[i]
                i+=1
            else:
                ans+=1
                sum=sum*2+1
        return ans
