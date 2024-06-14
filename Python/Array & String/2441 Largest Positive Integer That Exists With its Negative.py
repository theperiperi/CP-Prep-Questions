class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        ptr=len(nums)-1
        while ptr>=0:
            if nums[ptr]>0 and -1*nums[ptr] in nums:
                return nums[ptr]
            ptr-=1
        return -1
