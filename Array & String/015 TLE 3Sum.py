class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        j=len(nums)-1
        lst=set()
        while i<j:
            k=-1*(nums[j]+nums[i])
            if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[k]!= nums[i]:
                if k in nums:
                    lst.add((nums[i],nums[j],k))
                if nums[i]<nums[j]:
                    i+=1
                else:
                    j-=1
        return lst
        
