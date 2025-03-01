from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        non_zero_index = 0
        for num in nuxms:
            if num!=0:
                nums[non_zero_index] = num
                non_zero_index += 1
        
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

        return nums
