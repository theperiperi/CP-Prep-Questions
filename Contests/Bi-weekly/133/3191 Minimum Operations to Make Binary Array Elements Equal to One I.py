class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        flips = 0

        for i in range(n - 2):
            if nums[i] == 0:
                # Flip the current element and the next two elements
                for j in range(3):
                    nums[i + j] = 1 - nums[i + j]
                flips += 1

        # Check if the last two elements are 1s
        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return flips
            
        
