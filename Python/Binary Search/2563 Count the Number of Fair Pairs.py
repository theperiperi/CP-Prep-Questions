class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.countPairs(nums, upper) - self.countPairs(nums, lower-1)
    
    def countPairs(self, nums, target):
        count = 0
        left, right = 0, len(nums)-1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right-left
                left += 1
        return count
