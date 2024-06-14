class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #return nums.index(max(nums))

        #length 1, means one element
        if len(nums)==1:
            return 0

        #1st element greater than second, means first max
        if nums[0]>nums[1]:
            return 0
        
        #last element greater than second last, means last max
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        #ignore first and last element
        left=1
        right=len(nums)-2

        while left<=right:
            mid=left+(right-left)//2

            #check if middle greater than neighbors
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid-1]<nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return None
