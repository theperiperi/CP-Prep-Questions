class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        lst=set()
        ans=[]

        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1

            while j<k:
                sum1=nums[i]+nums[j]+nums[k]
                if sum1==0:
                    lst.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sum1<0:
                    j+=1
                else:
                    k-=1
        ans=list(lst)
        return ans

