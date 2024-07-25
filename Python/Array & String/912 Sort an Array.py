from random import randint
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(left, right):
            # Base case
            if left >= right:
                return
          
            # Choose a random pivot element from the segment.
            pivot = nums[randint(left, right)]
            less_than_pointer, greater_than_pointer, current = left - 1, right + 1, left
          
            # Iterate until 'current' is less than 'greater_than_pointer'.
            while current < greater_than_pointer:
                if nums[current] < pivot:
                    less_than_pointer += 1
                    nums[less_than_pointer], nums[current] = nums[current], nums[less_than_pointer]
                    current += 1
                elif nums[current] > pivot:                    
                    greater_than_pointer -= 1
                    nums[greater_than_pointer], nums[current] = nums[current], nums[greater_than_pointer]
                else:
                    current += 1

            quick_sort(left, less_than_pointer)
            quick_sort(greater_than_pointer, right)

        quick_sort(0, len(nums) - 1)
        return nums
