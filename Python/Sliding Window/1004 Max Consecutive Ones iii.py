class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left_pointer=0
        right_pointer=0
    
        while right_pointer<len(nums):
            if nums[right_pointer]==0:
                k-=1
            if k<0:
                if nums[left_pointer]==0:
                    k+=1
                left_pointer+=1
            right_pointer+=1
        length_of_window=right_pointer-left_pointer
        return length_of_window
        
