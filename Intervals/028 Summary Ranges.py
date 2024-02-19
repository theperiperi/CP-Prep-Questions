class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res=[]
        start=nums[0]
        end=start

        for i in range(len(nums)):
            if i!=len(nums)-1 and nums[i]+1==nums[i+1]:
                end=nums[i+1]
            else:
                if start<end:
                    res.append(str(start)+"->"+str(end))
                else:
                    res.append(str(start))
                if i!=len(nums)-1:
                    start=nums[i+1]

        return res
