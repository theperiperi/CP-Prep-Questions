class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        
        nums.sort()
        median = nums[len(nums) // 2]
        
        operations = sum(abs(num - median) // x for num in nums)
        
        return operations
