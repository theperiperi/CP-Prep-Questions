class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1  
