class Solution(object):
    def minIncrementForUnique(self,nums):
        nums.sort()
        moves = 0

        for i in range(1, len(nums)):
            j=i-1
            if nums[j]>=nums[i]:
                increment = nums[j] - nums[i] +1
                nums[i] = nums[j] + 1
                moves += increment

        return moves
