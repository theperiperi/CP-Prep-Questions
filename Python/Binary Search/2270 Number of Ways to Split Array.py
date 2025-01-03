class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = (sum(nums)+1)//2
        res = 0
        for i in range(len(nums)-1):
            left += nums[i]
            if left >= right:
                res += 1
        return res
