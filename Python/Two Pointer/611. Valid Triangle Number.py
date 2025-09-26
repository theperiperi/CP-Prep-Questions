class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for k in range(len(nums)-1,1,-1):
            right = nums[k]
            if nums[0]+nums[1]>right:
                ans+= (k+1)*k*(k-1)//6
                break
            if nums[k-1]+nums[k-2]<=right:
                continue
            left = 0
            mid = k-1
            while left<mid:
                if nums[left]+nums[mid]>right:
                    ans+=mid-left
                    mid-=1
                else:
                    left+=1
        return ans
