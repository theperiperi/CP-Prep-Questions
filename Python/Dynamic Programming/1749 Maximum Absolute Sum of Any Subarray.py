class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sums = list(accumulate(nums, initial=0))
        return max(sums) - min(sums)
