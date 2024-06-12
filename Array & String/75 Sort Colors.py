class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red = 0
        white = 0
        blue = 0

        for i in range(n):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else:
                blue += 1

        for i in range(n):
            if red != 0:
                nums[i] = 0
                red -= 1
            elif white != 0:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2    
        
