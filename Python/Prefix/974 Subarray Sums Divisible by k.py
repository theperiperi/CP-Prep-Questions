class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefix,res=0,0
        dp=[0]*k
        dp[0]=1

        for num in nums:
            prefix+=num
            prefix%=k
            res+=dp[prefix]
            dp[prefix]+=1
        return res
