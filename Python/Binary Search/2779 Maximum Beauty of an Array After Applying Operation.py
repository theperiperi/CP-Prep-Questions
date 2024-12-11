class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 1
        left = 0
        for right in range(1, len(nums)):
            if nums[right] - k > nums[left] + k:
                left += 1
            result = max(result, right - left + 1)
        return result
