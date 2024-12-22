class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while len(set(nums))!=len(nums):
            nums=nums[3:]
            count+=1
        return count
