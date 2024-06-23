class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        averages = []

        nums.sort()
        while len(nums) > 1:
            avg = (nums[0] + nums[-1]) / 2.0
            nums.pop(-1)
            nums.pop(0)
            averages.append(avg)
        
        return min(averages)
