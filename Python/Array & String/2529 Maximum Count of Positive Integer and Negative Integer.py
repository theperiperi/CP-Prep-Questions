class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count = 0
        zero = 0
        for i in nums:
            if i<0:
                count+=1
            elif i==0:
                zero+=1
            else:
                break
        return(max(count,len(nums)-zero-count))
