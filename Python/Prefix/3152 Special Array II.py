class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        prefix=[0]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1]
            if (nums[i-1]%2==nums[i]%2):
                prefix[i]+=1
        
        result=[]

        for left,right in queries:
            special_count = prefix[right]
            if left>0:
                special_count-=prefix[left]
            result.append(special_count==0)

        return result
